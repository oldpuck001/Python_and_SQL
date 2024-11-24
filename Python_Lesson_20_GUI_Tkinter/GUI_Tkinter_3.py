# GUI_Tkinter_3.py

import tkinter as tk

def print_value(val):
    print(f"Slider value: {val}")

def hello():
    print("你好！")

# 創建 Tk 的實例
root = tk.Tk()

# 設置窗口的大小與位置（+10+20' 設定了窗口左上角位於屏幕的(10, 20)位置）
root.geometry('960x720+50+50')

# Scale 滑塊
scale = tk.Scale(from_=0, to=100, command=print_value)
scale.pack()

# Canvas 畫布控件
# Canvas控件提供了一個二維的繪圖空間，你可以在上面繪製各種形狀，包括線、矩形、多邊形、橢圓、文本等。
# 也可以在Canvas上放置圖片和其他tkinter控件。
# 創建一個 Canvas 控件
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack()
# 在 Canvas 上畫一個矩形
canvas.create_rectangle(50, 20, 150, 80, fill="blue")
# 在 Canvas 上畫一條線
canvas.create_line(0, 0, 200, 100, fill="red", width=3)


# Menu 菜單
# 首先創建了一個Menu控件並將它設置為窗口的主菜單
# 然後創建子菜單並將它們添加到主菜單。子菜單中都有一些項目，當這些項目被選擇時，會調用 hello 函數。
# Menu 控件為應用程序提供了一個菜單系統。你可以在菜單中添加項目，並為每個項目定義一個回調函數，這個回調函數將在項目被選擇時被調用。
# 創建主菜單
menu = tk.Menu(root)
root.config(menu=menu)
# 創建一個子菜單並將它添加到主菜單
filemenu = tk.Menu(menu)
menu.add_cascade(label="文件", menu=filemenu)
# 在子菜單中添加一些項目
filemenu.add_command(label="打開", command=hello)
filemenu.add_command(label="保存", command=hello)


# PanedWindow 可以包含其他控件的窗口
# 首先創建一個PanedWindow控件，並將其設定為水平方向
# 然後在PanedWindow中添加了兩個Label控件。
# 這兩個Label控件會被放置在PanedWindow的兩個面板中，用戶可以拖動中間的分隔條來調整它們的相對大小。
# PanedWindow控件是一個可以包含其他控件的容器，它將其子控件排列在一個水平或垂直的行中。每個子控件都有一個相對於其鄰居的可調大小。
# 創建一個 PanedWindow
pw = tk.PanedWindow(root, orient="horizontal")
pw.pack(fill="both", expand=True)
# 在 PanedWindow 中添加兩個 Label 控件
left = tk.Label(pw, text="左側面板", bg="blue", fg="white")
pw.add(left)
right = tk.Label(pw, text="右側面板", bg="red", fg="white")
pw.add(right)


root.mainloop()