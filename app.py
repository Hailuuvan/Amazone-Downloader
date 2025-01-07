import requests

def download_image(image_url, save_path):
    try:
        # Gửi yêu cầu HTTP GET tới URL của ảnh
        response = requests.get(image_url)
        
        # Kiểm tra nếu yêu cầu thành công
        if response.status_code == 200:
            # Mở file ở chế độ ghi nhị phân và lưu ảnh
            with open(save_path, 'wb') as file:
                file.write(response.content)
            print(f"Ảnh đã được tải về thành công tại {save_path}")
        else:
            print(f"Lỗi: Không thể tải ảnh. Mã trạng thái: {response.status_code}")
    
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")

# Đường dẫn URL của ảnh
image_url = ' https://f.media-amazon.com/images/I/91Z9JdughZL.png'

# Đường dẫn lưu file ảnh trên máy tính
save_path = 'Image/downloaded.png'

# Gọi hàm để tải ảnh
download_image(image_url, save_path)
