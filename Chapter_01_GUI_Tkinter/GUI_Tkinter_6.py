# GUI_Tkinter_5.py

# 簡單的GUI界面

import tkinter as tk
from tkinter import filedialog
# event=None

# Open
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    print(file_path)

# Save
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text Files","*.txt"),("All Files","*.*")])
    print(file_path)

# select folder
def select_folder():
    folder_path = filedialog.askdirectory()
    print(folder_path)

top=tk.Tk()
top.title('GUI_Tkinter')

top.geometry('240x180+50+50')

tk.Button(text='Open',command=open_file).pack(side=tk.LEFT)
tk.Button(text='Save',command=save_file).pack(side=tk.LEFT)
tk.Button(text='Select Folder',command=select_folder).pack(side=tk.LEFT)

tk.mainloop()