from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Hàm tải và khởi tạo ChromeDriver
def get_driver():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")  # Mở ở chế độ ẩn danh
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.6613.114 Safari/537.36")

    # Tự động tải và cài đặt ChromeDriver phù hợp với phiên bản Chrome hiện tại
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# Ví dụ sử dụng
driver = get_driver()

# Điều hướng tới URL
driver.get("https://www.google.com")

# Đóng trình duyệt
driver.quit()

driver_path = ChromeDriverManager().install()

print(driver_path)