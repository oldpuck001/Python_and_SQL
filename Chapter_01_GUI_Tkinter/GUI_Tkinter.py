# GUI_Tkinter_1.py

import tkinter as tk

# 創建 Tk 的實例
root = tk.Tk()

# 設置窗口的標題
root.title("My Application")

# 設置窗口的大小與位置（+10+20' 設定了窗口左上角位於屏幕的(10, 20)位置）
root.geometry('1280x720+35+65')

# 設置窗口的最小大小
root.minsize(640, 360)

# 設置窗口的最大大小
root.maxsize(1280, 720)

# 設置窗口是否可以被用戶調整大小，兩個參數分別表示寬度和高度是否可以調整
root.resizable(True, True)


















# 在常規程序中，將調用函數mainloop以進入Tkinter主事件循環
# mainloop：進入消息循環，它會等待和處理窗口的各種事件，如鼠標點擊、鍵盤按壓等
root.mainloop()