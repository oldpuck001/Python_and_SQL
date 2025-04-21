# GUI_Tkinter_5.py

# 大型文本區域的控件：
# 要創建可滾動的多行文本區域，可結合使用控件Text和Scrollbar，但模塊tkinter.scrolledtext已經提供了一種實現。
# 對於ScrolledText對象，將使用其方法delete和insert來刪除文本。
# 調用方法delete和insert時，需要使用合適的參數來指定文本的位置。
# 例如，使用‘1.0’來指定第1行的第0個字符（即第一個字符前面），使用END來指定文本末尾，並使用INSERT來指定當前插入點。

# 簡單的GUI文本編輯器

import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
from tkinter.filedialog import askopenfilename,asksaveasfilename

# Initialize file path
global file_path
file_path = ''

# Open
def open_file(event=None):
    global file_path
    if contents.get('1.0',tk.END) != '\n':
        answer = messagebox.askyesnocancel("Save changes?", "Do you want to save changes?")
        if answer is True:
            save_file()
        elif answer is False:
            pass            
        else:
            return
    file_path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        contents.delete('1.0', tk.END)
        with open(file_path, 'r') as input_file:
            contents.insert(tk.INSERT, input_file.read())
    top.title("Text Editor - " + file_path)


# Save
def save_file(event=None):
    global file_path
    if not file_path:
        save_as_file()
    else:
        with open(file_path, 'w') as output_file:
            output_file.write(contents.get('1.0',tk.END+'-1c'))
    top.title("Text Editor - " + file_path)


# Save As…
def save_as_file(event=None):
    global file_path
    file_path = asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    if file_path:
        with open(file_path, 'w') as output_file:
            output_file.write(contents.get('1.0',tk.END+'-1c'))
    top.title("Text Editor - " + file_path)


top=tk.Tk()
top.title("Simple Editor")

contents = ScrolledText(top)
contents.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

tk.Button(text='Open',command=open_file).pack(side=tk.LEFT)
tk.Button(text='Save',command=save_file).pack(side=tk.LEFT)
tk.Button(text='Save as…',command=save_as_file).pack(side=tk.LEFT)

tk.mainloop()