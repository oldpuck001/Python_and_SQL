# fetchall_py.py

import sqlite3

# 連接資料庫
conn = sqlite3.connect('example.db')
curs = conn.cursor()

# 建立範例表格和插入數據
curs.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)')
curs.execute('INSERT INTO users (id, name) VALUES (1, "Alice"), (2, "Bob")')

# 查詢數據
curs.execute('SELECT * FROM users')

# 提取所有行
rows = curs.fetchall()
print(rows)  # 輸出：[(1, 'Alice'), (2, 'Bob')]

# 關閉連接
conn.close()


# 當結果為空
# curs.execute('SELECT * FROM users WHERE id = 100')
# rows = curs.fetchall()
# print(rows)
# 輸出：[]