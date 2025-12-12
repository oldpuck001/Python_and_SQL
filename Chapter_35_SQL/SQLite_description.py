# SQLite_description.py

# 獲取欄位名稱

import os
import sqlite3

path = os.path.join('/Users/lei/Downloads', 'example.db')

# 連接資料庫
conn = sqlite3.connect(path)
curs = conn.cursor()

# 建立表格並插入數據
curs.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT, age INTEGER)')
curs.execute('INSERT INTO users (id, name, age) VALUES (1, "Alice", 30)')

# 執行查詢
curs.execute('SELECT * FROM users')

# 獲取欄位資訊
print(curs.description)

# 提取欄位名稱
column_names = [col[0] for col in curs.description]
print(column_names)                                     # 輸出：['id', 'name', 'age']

# 關閉連接
conn.close()