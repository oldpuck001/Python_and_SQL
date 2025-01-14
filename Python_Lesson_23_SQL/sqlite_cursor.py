# sqlite_sursor.py

import os
import sqlite3

path = os.path.join('/Users/lei/Downloads', 'somedatabase.db')

# 直接連接到數據庫
conn = sqlite3.connect(path)

# 直接執行 SQL 查詢
conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

# 插入數據
conn.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))

# 提交修改
conn.commit()

# 關閉連接
conn.close()

'''
在 SQLite 中，可以直接使用conn.execute()方法執行SQL查詢，而無需明確創建游標(cursor)物件。
這種方式適合簡單的查詢或操作，但對於需要多次重複執行查詢或需要更複雜的控制時，游標仍然是比較推薦的方式。
何時使用cursor()？
簡單查詢：可直接用conn.execute()
複雜查詢或多次執行：建議使用cursor()，如：
需要fetchall()、fetchone()來獲取查詢結果。
需要重複執行多個SQL語句。
這種方式讓程式更簡潔，但仍需根據具體需求選擇適合的方式。
'''