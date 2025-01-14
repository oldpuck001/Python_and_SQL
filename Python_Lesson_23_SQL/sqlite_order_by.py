# sqlite_order_by.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

# 在指定一条ORDER BY子句时，应该保证它是SELECT语句中最后一条子句。如果它不是最后的子句，将会出现错误消息。
ob_1 = curs.execute('SELECT prod_name FROM Products ORDER BY prod_name;')               # 按單一列排序

for row in ob_1:
    print(row)

ob_2 = curs.execute('SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price, prod_name;')  # 按多個列排序

for row in ob_2:
    print(row)

ob_3 = curs.execute('SELECT prod_id, prod_price, prod_name FROM Products ORDER BY 2, 3;')       # 使用列位置

for row in ob_3:
    print(row)

ob_4 = curs.execute('SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC;')       # 指定排序方向

for row in ob_4:
    print(row)

# DESC 是 DESCENDING 的缩写，这两个关键字都可以使用。如果想在多个列上进行降序排序，必须对每一列指定 DESC 关键字。
ob_5 = curs.execute('SELECT prod_id, prod_price, prod_name FROM Products ORDER BY prod_price DESC,prod_name;')  # 多列指定排序方向

for row in ob_5:
    print(row)

conn.close()