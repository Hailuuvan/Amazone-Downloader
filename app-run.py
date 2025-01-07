import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time
import re

def get_product_details_from_asin(asin):
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Mở ở chế độ ẩn danh
    chrome_options.add_argument("--headless")  # Chạy Chrome ở chế độ nền (không hiển thị)
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.114 Safari/537.36")

    #chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

    driver_path = r"C:\\Users\\msi\AppData\\Local\\Google\\chromedriver-win64\\chromedriver.exe"
    service = Service(driver_path)
    
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        url = f"https://www.amazon.com/dp/{asin}"
        driver.get(url)

        time.sleep(3)

        # Lấy tiêu đề sản phẩm
        title_element = driver.find_element(By.XPATH, '//*[@id="productTitle"]')
        title = title_element.text.strip()
        
        # Chuyển tiêu đề thành tên file hợp lệ
        safe_title = re.sub(r'[\/:*?"<>|]', '', title)  # Loại bỏ các ký tự không hợp lệ
        file_name = f"Image/{safe_title}.png" # Đổi vị trí lưu ảnh

        # Tìm thẻ <img> chứa URL hình ảnh sản phẩm
        img_wrapper = driver.find_element(By.XPATH, '//*[@id="imgTagWrapperId"]')
        img_tag = img_wrapper.find_element(By.TAG_NAME, 'img')
        image_data = img_tag.get_attribute('data-a-dynamic-image')

        if image_data:
            image_url = list(eval(image_data).keys())[0]
            return image_url, file_name
        else:
            print(f"Không tìm thấy ảnh cho ASIN {asin}.")
            return None, None
        
    except Exception as e:
        print(f"Đã xảy ra lỗi khi truy cập trang với ASIN {asin}: {e}")
        return None, None
    
    finally:
        driver.close()

def extract_modified_image_url(original_url):
    parts = original_url.split('%7C')
    
    if len(parts) >= 3:
        third_element = parts[2]
        new_image_url = f"https://m.media-amazon.com/images/I/{third_element}"
        return new_image_url
    else:
        print("URL không có đủ phần tử phân cách bằng %7C.")
        return None

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Ảnh đã được tải về thành công tại {save_path}")
        else:
            print(f"Lỗi: Không thể tải ảnh. Mã trạng thái: {response.status_code}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

def process_asins_from_excel(file_path):
    # Đọc file Excel
    df = pd.read_excel(file_path)
    asins = df['ASIN'].tolist()  # Giả sử cột chứa ASIN tên là 'ASIN'

    for asin in asins:
        print(f"Đang xử lý ASIN: {asin}")
        original_image_url, file_name = get_product_details_from_asin(asin)
        if original_image_url and file_name:
            modified_image_url = extract_modified_image_url(original_image_url)
            if modified_image_url:
                download_image(modified_image_url, file_name)

# Đường dẫn tới file Excel chứa danh sách ASIN
file_path = 'data.xlsx'  # Thay đổi thành đường dẫn thực tế tới file Excel

process_asins_from_excel(file_path)