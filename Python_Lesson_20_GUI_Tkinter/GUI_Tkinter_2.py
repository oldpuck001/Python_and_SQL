# GUI_Tkinter_2.py

import tkinter as tk

root = tk.Tk()

# 這段代碼創建的窗口，包含一個Scrollbar和一個Listbox。往Listbox中插入了100個項目，使其超過了可視區域的範圍。
# 然後，使用Scrollbar來滾動Listbox的內容，使我們能夠查看所有的項目。
# 創建 Scrollbar
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# 創建 Listbox
listbox = tk.Listbox(root, yscrollcommand=scrollbar.set)
for i in range(100):
    listbox.insert(tk.END, str(i))
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# 將 Scrollbar 鏈接到 Listbox
scrollbar.config(command=listbox.yview)

root.mainloop()