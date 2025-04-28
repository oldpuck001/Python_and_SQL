# sqlite_aggregate_function.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

'''
SQL 聚集函数
函数         说明
AVG()       返回某列的平均值
COUNT()     返回某列的行数
MAX()       返回某列的最大值
MIN()       返回某列的最小值
SUM()       返回某列值之和
'''

# AVG()函数忽略列值为 NULL 的行。
ag_1 = curs.execute("SELECT AVG(prod_price) AS avg_price FROM Products;")

for row in ag_1:
    print(row)

ag_2 = curs.execute("SELECT AVG(prod_price) AS avg_price FROM Products WHERE vend_id = 'DLL01';")

for row in ag_2:
    print(row)

# 使用 COUNT(*)对表中行的数目进行计数，不管表列中包含的是空值（NULL）还是非空值。
ag_3 = curs.execute("SELECT COUNT(*) AS num_cust FROM Customers;")

for row in ag_3:
    print(row)

# 使用 COUNT(column)对特定列中具有值的行进行计数，忽略 NULL 值。
ag_4 = curs.execute("SELECT COUNT(cust_email) AS num_cust FROM Customers;")

for row in ag_4:
    print(row)

# MAX()返回指定列中的最大值。MAX()要求指定列名。MAX()函数忽略列值为NULL的行。
ag_5 = curs.execute("SELECT MAX(prod_price) AS max_price FROM Products;")

for row in ag_5:
    print(row)

# MIN()返回指定列的最小值。MIN()要求指定列名。MIN()函数忽略列值为NULL的行。
ag_6 = curs.execute("SELECT MIN(prod_price) AS min_price FROM Products;")

for row in ag_6:
    print(row)

# SUM()用来返回指定列值的和（总计）。
ag_7 = curs.execute("SELECT SUM(quantity) AS items_ordered FROM OrderItems WHERE order_num = 20005;")

for row in ag_7:
    print(row)

# SUM()函数忽略列值为 NULL 的行。
ag_8 = curs.execute("SELECT SUM(item_price*quantity) AS total_price FROM OrderItems WHERE order_num = 20005;")

for row in ag_8:
    print(row)

# 只包含不同的值，指定DISTINCT参数。
ag_9 = curs.execute("SELECT AVG(DISTINCT prod_price) AS avg_price FROM Products WHERE vend_id = 'DLL01';")

for row in ag_9:
    print(row)

# 包含多个聚集函数
ag_10 = curs.execute("SELECT COUNT(*) AS num_items, MIN(prod_price) AS price_min, MAX(prod_price) AS price_max, AVG(prod_price) AS price_avg FROM Products;")

for row in ag_10:
    print(row)

# 在指定别名以包含某个聚集函数的结果时，不应该使用表中实际的列名。虽然这样做也算合法，但许多 SQL 实现不支持，可能会产生模糊的错误消息。

conn.close()