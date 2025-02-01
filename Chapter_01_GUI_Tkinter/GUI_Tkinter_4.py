# GUI_Tkinter_4.py

import tkinter as tk
from tkinter import messagebox

def create_new_window():
    new_window = tk.Toplevel(root)
    label = tk.Label(new_window, text="這是一個新的窗口")
    label.pack()

def ask_save_changes():
    answer = messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
    if answer is True:                      # Save changes
        print("Save changes")               # 在這裡實現保存文件的功能
    elif answer is False:                   # Don't save changes
        print("Don't save changes")         # 在這裡實現不保存變化，繼續打開新文件的功能
    else:                                   # Cancel
        print("Cancel opening new file")    # 在這裡實現取消打開新文件的功能

def print_hello(event):
    print('Hello, World!')

root = tk.Tk()

# 設置窗口的大小與位置（+10+20' 設定了窗口左上角位於屏幕的(10, 20)位置）
root.geometry('400x300+50+50')

# Toplevel 創建子窗口
# 首先創建了一個主窗口，然後添加了一個按鈕，當按鈕被點擊時，會調用create_new_window函數。
# 在這個函數中，創建了一個Toplevel窗口並在其中添加了一個標籤。
# Toplevel控件可以用來創建額外的窗口。每個Toplevel窗口都是一個獨立的窗口，它有自己的標題和圖標，並可以包含其他的tkinter控件。
button_1 = tk.Button(root, text="創建新的窗口", command=create_new_window)
button_1.pack()


# messagebox模塊
# 在這段代碼中，askyesnocancel 函數會彈出一個對話框，有 "Yes", "No" 和 "Cancel" 三個按鈕。
# 如果用戶點擊 "Yes"，函數將返回 True；如果用戶點擊 "No"，函數將返回 False；如果用戶點擊 "Cancel" 或關閉對話框，函數將返回 None。
# 可以根據函數的返回值來決定進行什麼操作。
button_2 = tk.Button(root, text="打開選擇窗口", command=ask_save_changes)
button_2.pack()


# pack包管理器
button_3 = tk.Button(root, text="Button 1")
button_3.pack(side="left", fill="y")

button_4 = tk.Button(root, text="Button 2")
button_4.pack(side="top", fill="x", expand=True)

button_5 = tk.Button(root, text="Button 3")
button_5.pack(side="right", anchor="s", padx=10, pady=20)


# 設置按鈕的command屬性
# 按鈕的command屬性用於指定單擊按鈕時要執行的函數。這個函數可以是自定義函數。
# 創建一個按鈕，點擊時銷毀窗口
# bind 綁定事件到特定的處理函數
# destroy 銷毀窗口，結束 mainloop
# quit 退出窗口的主事件循環
# 也可使用控件的構造函數來配置控件。例如：Button(text='Click me too!',command=clicked).pack() # clicked是自定義函數
exit_button = tk.Button(root, text='Exit', command=root.destroy)
exit_button.pack()


# bind 方法，當按鈕被單擊時，調用 print_hello 函數
button = tk.Button(root, text='Click me')
button.pack()
button.bind('<Button-1>', print_hello)


root.mainloop()