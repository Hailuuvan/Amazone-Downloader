import requests
from bs4 import BeautifulSoup

def get_image_url_from_asin(asin):
    # Bước 1: Truy cập trang sản phẩm Amazon
    url = f"https://www.amazon.com/dp/{asin}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        # Kiểm tra nếu truy cập thành công
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Bước 2: Phân tích HTML để tìm link ảnh
            image_tag = soup.find('img', {'id': 'landingImage'})  # Tìm thẻ <img> với id 'landingImage'
            
            if image_tag and 'src' in image_tag.attrs:
                image_url = image_tag['src']
                print(f"URL ảnh gốc tìm thấy: {image_url}")
                return image_url
            else:
                print("Không tìm thấy ảnh sản phẩm.")
                return None
        
        else:
            print(f"Lỗi: Không thể truy cập trang. Mã trạng thái: {response.status_code}")
            return None
    
    except Exception as e:
        print(f"Đã xảy ra lỗi khi truy cập trang: {e}")
        return None

def extract_modified_image_url(original_url):
    # Bước 3: Tìm các dấu | (%7C) và lấy phần tử thứ 3
    parts = original_url.split('%7C')
    
    if len(parts) >= 3:
        third_element = parts[2]
        new_image_url = f"https://m.media-amazon.com/images/I/{third_element}"
        print(f"URL ảnh đã chỉnh sửa: {new_image_url}")
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

# ASIN của sản phẩm
asin = "B0DF4YG6BD"

# Bước 4: Lấy URL ảnh từ ASIN và tải về
original_image_url = get_image_url_from_asin(asin)

if original_image_url:
    # Bước 5: Lọc URL và tải ảnh mới
    modified_image_url = extract_modified_image_url(original_image_url)
    if modified_image_url:
        download_image(modified_image_url, 'Image/downloaded_image.png')
