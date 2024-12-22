# SQLite_py.py

import os
import sqlite3

path = os.path.join('/Users/lei/Downloads', 'somedatabase.db')

# 創建直接到數據庫文件的連接（可以是文件的相對路徑或絕對路徑）
# 如果指定的文件不存在，將自動創建它
conn = sqlite3.connect(path)

# 從連接獲取游標
curs = conn.cursor()

# 游標可用來執行SQL查詢
# 執行完查詢後，如果修改了數據，務必提交所做的修改，這樣才會將其保存到文件中
conn.commit()

# 應該在每次修改數據庫後都進行提交，而不是僅在要關閉連接前才這樣做
# 要關閉連接，只需調用方法close。
conn.close()