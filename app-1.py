import requests

# Link media sản phẩm từ Amazon
media_link = "https://f.media-amazon.com/images/I/A1dbsmzbGeL._CLa%7C2140%2C2000%7C91Z9JdughZL.png%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX385_.png"

# Lọc bỏ các phần tử không mong muốn
start_pattern = "A1dbsmzbGeL._CLa%7C2140%2C2000%7C"
end_pattern = "%7C0%2C0%2C2140%2C2000%2B0.0%2C0.0%2C2140.0%2C2000.0_AC_SX385_.png"

filtered_link = media_link.replace(start_pattern, "").replace(end_pattern, "")

# Tải ảnh từ URL đã lọc
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

# Đường dẫn lưu file ảnh trên máy tính
save_path = 'Image/downloaded.png'

# Gọi hàm để tải ảnh
download_image(filtered_link, save_path)
