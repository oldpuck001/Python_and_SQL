# GUI_Tkinter_1.py

import tkinter as tk

def selection(value):
    print("你選擇了", value)


# 創建 Tk 的實例
root = tk.Tk()

# 設置窗口的標題
root.title("My Application")

# 設置窗口的大小與位置（+10+20' 設定了窗口左上角位於屏幕的(10, 20)位置）
root.geometry('960x720+50+50')

# 設置窗口的最小大小
root.minsize(200, 100)

# 設置窗口的最大大小
root.maxsize(1920, 1080)

# 設置窗口是否可以被用戶調整大小，兩個參數分別表示寬度和高度是否可以調整
root.resizable(True, True)

# configure 或者 config：修改窗口的屬性，如背景顏色等
# 在Tkinter中，config方法用於修改控件（如按鈕、標籤、文本框等）的屬性。
# 可以使用方法config同時設置多個屬性。
# 可以使用config方法來更改控件的外觀和行為，例如文字、顏色、尺寸等。
# btn.config(text='Click me!',comand=clicked)
# 在 Tkinter 中，config 和 configure 實際上是同一個方法，它們的功能和用法完全相同。
# 你可以使用這個方法來修改 Tkinter 控件的配置選項。
root.configure(bg='lightblue')


# 創建一個 Frame框架，框架用於控制布局
frame_1 = tk.Frame(root)
frame_1.pack()

# 在 Frame 中創建一個 Label，Label標籤用於顯示文字或圖片
label_1 = tk.Label(frame_1, text="This is a label inside a LabelFrame")
label_1.pack()

# 創建一個 LabelFrame 框架，LabelFrame 框架可以為其內部的控件提供一個可見的邊界，並且邊界的頂部可以有一個標題。
frame_2 = tk.LabelFrame(root, text="This is a LabelFrame", padx=10, pady=10)
frame_2.pack(padx=10, pady=10)

# 在 LabelFrame 中創建一個 Label，Label標籤用於顯示文字或圖片
label_2 = tk.Label(frame_2, text="This is a label inside a LabelFrame")
label_2.pack()

# Message 控件，與Label 控件很相似，但是提供了自動文本包裝的功能，例如換行，所以特別適合用於顯示長文本
message = tk.Message(root, text='這是一條長消息，它將被自動包裝以適應給定的寬度。', width=100)
message.pack()

# Button
button = tk.Button(root, text="This is a button.")
button.pack()

# Entry 單行文本框，提取內容使用方法get
entry = tk.Entry(root)
entry.pack()

# Text 文字區域，用於顯示和處理多行文字，提取內容使用方法get
text = tk.Text(root, height=5, width=30)
text.pack()

# Spinbox 輸入框，可以選擇數字或者文字
spin = tk.Spinbox(root, from_=0, to=10)
spin.pack()

# Listbox 列表框
listbox_1 = tk.Listbox(root)
listbox_1.insert(1, "Option 1")
listbox_1.insert(2, "Option 2")
listbox_1.pack()


# OptionMenu 下拉菜單
# 首先創建了一個 StringVar 對象來保存選擇的選項。
# 然後，創建了一個 OptionMenu 控件，並將選項列表和 StringVar 對象傳遞給它。
# 最後，設置初始選擇的值，並通過 pack 方法添加了控件。
# 創建一個 StringVar 對象來保存選擇的值
selected_option = tk.StringVar(root)
# 創建一個 OptionMenu 控件
options = ['選項1', '選項2', '選項3']
option_menu = tk.OptionMenu(root, selected_option, *options, command=selection)
# 設置初始選擇的值
selected_option.set(options[0])
option_menu.pack()


# Menubutton 菜單按鈕
# 首先創建一個Menubutton控件並將它添加到窗口中
# 然後創建一個Menu控件並將它與Menubutton控件關聯
# 最後，在Menu中添加了一些項目，當這些項目被選擇時，會打印一條消息到控制臺
# 創建一個 Menubutton 控件
mb = tk.Menubutton(root, text="選單按鈕", relief="raised")
mb.pack()
# 創建一個 Menu 控件，並將它與 Menubutton 控件關聯
menu = tk.Menu(mb, tearoff=0)
mb["menu"] = menu
# 在 Menu 中添加一些項目
menu.add_command(label="選項1", command=lambda: print("你選擇了選項1"))
menu.add_command(label="選項2", command=lambda: print("你選擇了選項2"))


# Checkbutton 多選按鈕
check = tk.Checkbutton(root, text="Checkbutton")
check.pack()

# Radiobutton 單選按鈕
radio1 = tk.Radiobutton(root, text="Radio1", value=1)
radio1.pack()
radio2 = tk.Radiobutton(root, text="Radio2", value=2)
radio2.pack()


# 在常規程序中，將調用函數mainloop以進入Tkinter主事件循環
# mainloop：進入消息循環，它會等待和處理窗口的各種事件，如鼠標點擊、鍵盤按壓等
root.mainloop()