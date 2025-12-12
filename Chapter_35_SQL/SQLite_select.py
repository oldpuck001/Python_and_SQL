# SQLite_select.py

import sqlite3

# 創建直接到數據庫文件的連接（可以是文件的相對路徑或絕對路徑）
# 如果指定的文件不存在，將自動創建它
conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

# 從連接獲取游標
curs = conn.cursor()

# SQL語句不區分大小寫，習慣上指令使用大寫，單行查詢語句可以不加分號
select_1 = curs.execute('SELECT prod_name FROM Products;    --註釋')                 # 檢索單個列
select_1_1 = curs.execute('/*SELECT prod_name FROM Products;*/')                    # 註釋

for row in select_1:
    print(row)

select_2 = curs.execute('SELECT prod_id, prod_name, prod_price FROM Products;')     # 檢索多個列，用逗號隔開

for row in select_2:
    print(row)

select_3 = curs.execute('SELECT * FROM Products;')                                  # 檢索所有列

for row in select_3:
    print(row)

select_4 = curs.execute('SELECT DISTINCT vend_id FROM Products;')   # 返回所有唯一值，如過關鍵字後面是兩個列，則除非兩個列完全相同，否會返回所有列

for row in select_4:
    print(row)

select_5 = curs.execute('SELECT prod_name FROM Products LIMIT 5;')            # 返回前5行

for row in select_5:
    print(row)

select_6 = curs.execute('SELECT prod_name FROM Products LIMIT 5 OFFSET 2;')   # 從2（第1個行是0）行開始返回5行

for row in select_6:
    print(row)

# 應該在每次修改數據庫後都進行提交，而不是僅在要關閉連接前才這樣做
# 要關閉連接，只需調用方法close。
conn.close()