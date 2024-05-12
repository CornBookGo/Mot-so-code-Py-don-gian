import os

# Đường dẫn đến thư mục chứa ảnh
folder_path = "PureMedia Vol.234 Yeha 예하 - Karaoke Hentai CallGirl B"
file_extension = ".jpg"  # Định dạng tệp tin ảnh của bạn
start_index = 40  # Số bắt đầu bạn muốn sử dụng

# Lặp qua tất cả các tệp tin trong thư mục
count = start_index
for filename in os.listdir(folder_path):
    if filename.endswith(file_extension):
        src = os.path.join(folder_path, filename)
        dst = os.path.join(folder_path, str(count) + file_extension)
        # Thực hiện việc đổi tên tệp tin
        os.rename(src, dst)
        count += 1
        # Chỉ chuyển tên ảnh đến 100
        if count > 1000:
            break
print("Đã chuyển xong tên ảnh")