# đặt thư viện
from pytube import YouTube 
import os 
  
# đường dẫn video để tải
yt = YouTube( 
    str(input("Đặt đường dẫn video muốn tải: \n>> "))) 
  
# chỉ chọn nhạc
video = yt.streams.filter(only_audio=True).first() 
  
# đặt điểm chỗ tải
print("Đặt điểm tải (để trống cho thư mục hiện tại)") 
destination = str(input(">> ")) or '.'
  
# tải tệp
out_file = video.download(output_path=destination) 
  
# lưu tệp
base, ext = os.path.splitext(out_file) 
new_file = base + '.mp3'
os.rename(out_file, new_file) 
  
# đưa ra kết quả thành công
print(yt.title + " đã được tải thành công.")