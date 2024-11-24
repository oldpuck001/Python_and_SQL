# os_path_py.py

import os

targetPath_1 = '/Users/lei/Downloads/自动改名程序'
targetPath_2 = '/Users/lei/Downloads/del'
targetPath_3 = '/Users/lei/Downloads/'
targetPath_5 = '/Users/lei/Downloads/a.txt'


# 检查路径是否存在
if os.path.exists(targetPath_1):
    print(f"目标路径'{targetPath_1}'已存在。")
else:
    # 安全地创建目录，即使目录已存在
    os.makedirs(targetPath_1, exist_ok=True)


# 检查路径是否是目錄
if os.path.isdir(targetPath_2):
    print(f"目标路径'{targetPath_2}'是文件夾。")


# 指定目錄中的所有文件和目錄名的列表
sorted_list = sorted(os.listdir(targetPath_3))
print(sorted_list)


# 合并路径
targetPath_4 = os.path.join(targetPath_3, 'a')
os.makedirs(targetPath_4, exist_ok=True)


# 返回给定路径的上级目录
print(os.path.dirname(targetPath_1))


# 將檔案路徑分成兩部分
head, tail = os.path.split(targetPath_5)
print('Head:', head)
print('Tail:', tail)

split_path = os.path.split(targetPath_5)
print('Head:', split_path[0])
print('Tail:', split_path[1])