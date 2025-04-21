# read_save_csv.py

import pandas as pd
import tkinter as tk
from tkinter import filedialog

# Open
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[('CSV Files', '*.csv'), ('All Files', '*.*')])
    # 也可以是URL地址

    # read_csv 方法導入csv文件，sep=',' 默認值是 , 逗號，可以省略成 df = pd.read_csv(file_path)
    df = pd.read_csv(file_path, sep=',')
    print(df)

    # df.info() 提供数据点数量、索引类型、 dtype 和内存占用信息
    print(df.info())

    # df.describe() 提供基本的统计数据，包括总数、均值、标准差、最小值、最大值和百分位数
    print(df.describe())

    # df.head(n=5) 返回 DataFrame 的前 n 行
    print(df.head(n=5))

    # df.tail(n=5) 返回 DataFrame 的最后 n 行
    print(df.tail(n=5))

    # df.dtypes 返回每一列的 dtype
    print(df.dtypes)

# Save
def save_file():
    columns = ['name', 'No.', 'country', 'score', 'job']
    index = [1001, 1000, 1002, 1003]
    data = [['Mike', 1, 'Thailand', 80, 'teacher'],
            ['Yang', 2, 'China', 77, 'student'],
            ['Tom', 3, 'England', 85, 'student'],
            ['Losa', 4, 'Japan', 90, 'accounting']]
    df = pd.DataFrame(data, columns=columns, index=index)
    file_path = filedialog.asksaveasfilename(defaultextension='.csv',filetypes=[('CSV Files','*.csv'),('All Files','*.*')])

    # to_csv 方法導出csv文件
    df.to_csv(file_path)

top=tk.Tk()
top.title('GUI_Tkinter')

tk.Button(text='import CSV File',command=open_file).pack(side=tk.LEFT)
tk.Button(text='export CSV File',command=save_file).pack(side=tk.LEFT)

tk.mainloop()