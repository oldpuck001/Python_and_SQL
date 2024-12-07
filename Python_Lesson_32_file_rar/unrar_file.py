# unrar_file.py

import os
import patoolib

# 指定 .rar 文件的路徑
rar_file_path = '/Users/lei/Downloads/6500系列打包(A08).rar'

# 指定解壓縮的目標目錄
output_directory = '/Users/lei/Downloads/unpacked'

# 如果目標目錄不存在，創建該目錄
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# 解壓縮 .rar 文件
try:
    patoolib.extract_archive(rar_file_path, outdir=output_directory)
    print(f'{rar_file_path} 解壓縮到 {output_directory} 成功！')

except Exception as e:
    print(f"解壓縮失敗：{e}")