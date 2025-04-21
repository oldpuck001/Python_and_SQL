README.md

在 Python 中，有多個主流的視頻處理庫，可以根據需求選擇合適的庫進行視頻處理。以下是一些常用的視頻處理庫及其簡要介紹：

1. OpenCV
用途：圖像處理與視頻處理  
特點：
開源且功能強大，支持多平台。
提供豐富的 API，用於讀取、處理和保存視頻。
支持實時視頻處理（例如攝像頭捕獲）。
提供了豐富的圖像處理工具，例如邊緣檢測、特徵提取等。

安裝

pip install opencv-python opencv-python-headless

示例代碼：

import cv2

# 打開視頻文件
cap = cv2.VideoCapture('video.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 顯示視頻幀
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


2. MoviePy
用途：簡單的視頻編輯與處理  
特點：
支持視頻剪輯、合併、特效處理。
可以輕鬆生成動畫 GIF 或導出視頻。
與音頻同步處理的功能良好。

安裝：

pip install moviepy

示例代碼：

from moviepy.editor import VideoFileClip

# 加載視頻
clip = VideoFileClip("video.mp4")

# 裁剪視頻前10秒
short_clip = clip.subclip(0, 10)

# 保存為新文件
short_clip.write_videofile("output.mp4")


3. FFmpeg-python
用途：高效視頻處理與格式轉換  
特點：
是FFmpeg的Python封裝，功能全面且高效。
支持多種視頻格式和轉碼功能。
適合需要高度自定義和批量處理的場景。

安裝：

pip install ffmpeg-python


示例代碼：

import ffmpeg

# 將視頻轉換為另一種格式
ffmpeg.input('input.mp4').output('output.avi').run()


4. imageio
用途：圖像和視頻讀取、寫入  
特點：
簡單易用，適合處理基礎視頻操作。
可用於創建動畫GIF和處理視頻幀。

安裝：

pip install imageio[ffmpeg]

示例代碼：

import imageio

# 讀取視頻並打印幀數
reader = imageio.get_reader('video.mp4')
for i, frame in enumerate(reader):
    print(f"Processing frame {i}")


5. PyAV
用途：高性能視頻與音頻處理  
特點：
基於 FFmpeg，功能強大。
提供了更底層的 API，適合需要自定義操作的用戶。
支持多種視頻編解碼格式。

安裝：

pip install av

示例代碼：

import av

# 打開視頻文件
container = av.open('video.mp4')
for frame in container.decode(video=0):
    print(frame)


6. Scikit-Video
用途：與NumPy結合的視頻處理  
特點：
與 NumPy和SciPy集成良好，適合科學計算。
提供簡單的讀寫視頻功能。

安裝：

pip install sk-video

示例代碼：

import skvideo.io

# 讀取視頻
video_data = skvideo.io.vread('video.mp4')
print(video_data.shape)  # (num_frames, height, width, num_channels)


7. Manim
用途：動畫視頻製作  
特點：
特別適合數學動畫和教學視頻製作。
使用LaTeX排版文字，創建高品質動畫。

安裝：

pip install manim

示例代碼：

from manim import Scene, Square

class CreateSquare(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))


比較與選擇建議
| 庫名稱        | 特點                                 | 適用場景                     |
|--------------|-------------------------------------|-----------------------------|
| OpenCV       | 功能全面，實時處理                     | 圖像處理、實時視頻處理         |
| MoviePy      | 簡單易用，適合快速視頻剪輯              | 簡單視頻編輯與處理             |
| FFmpeg-python| 高性能，支持格式轉換與轉碼              | 批量處理、高效轉碼             |
| imageio      | 入門簡單，支持基礎操作                  | 動畫 GIF、視頻幀處理          |
| PyAV         | 底層接口，支持高性能處理                | 高度自定義處理                |
| Scikit-Video | 與 NumPy 集成良好，支持科學計算         | 科學計算相關處理              |
| Manim        | 動畫製作工具，專注數學和教學動畫          | 教學視頻、動畫創作            |