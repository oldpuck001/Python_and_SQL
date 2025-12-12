# SQLite_where.py

import sqlite3

'''
操作符       说明
=           等于
<>          不等于
!=          不等于
<           小于
<=          小于等于
!           不小于
>           大于
>=          大于等于
!>          不大于
BETWEEN     在指定的两个值之间
IS NULL     为 NULL 值
'''

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

# 同时使用 ORDER BY 和 WHERE 子句时，应该让 ORDER BY 位于 WHERE 之后，否则将会产生错误
wh_1 = curs.execute('SELECT prod_name, prod_price FROM Products WHERE prod_price = 3.49;')

for row in wh_1:
    print(row)

wh_2 = curs.execute('SELECT prod_name, prod_price FROM Products WHERE prod_price < 10;')

for row in wh_2:
    print(row)

wh_3 = curs.execute("SELECT vend_id, prod_name FROM Products WHERE vend_id <> 'DLL01';")

for row in wh_3:
    print(row)

wh_4 = curs.execute("SELECT vend_id, prod_name FROM Products WHERE vend_id != 'DLL01';")

for row in wh_4:
    print(row)

# BETWEEN 匹配范围中所有的值，包括指定的开始值和结束值，两个值必须用 AND 关键字分隔。
wh_5 = curs.execute('SELECT prod_name, prod_price FROM Products WHERE prod_price BETWEEN 5 AND 10;')

for row in wh_5:
    print(row)

wh_6 = curs.execute('SELECT cust_name FROM CUSTOMERS WHERE cust_email IS NULL;')

for row in wh_6:
    print(row)

wh_7 = curs.execute("SELECT prod_id, prod_price, prod_name FROM Products WHERE vend_id = 'DLL01' AND prod_price <= 4;")

for row in wh_7:
    print(row)

wh_8 = curs.execute("SELECT prod_name, prod_price FROM Products WHERE vend_id = 'DLL01' OR vend_id = 'BRS01';")

for row in wh_8:
    print(row)

wh_9 = curs.execute("SELECT prod_name, prod_price FROM Products WHERE (vend_id = 'DLL01' OR vend_id = 'BRS01') AND prod_price >= 10;")

for row in wh_9:
    print(row)

# IN的最大优点是可以包含其他SELECT语句，能够更动态地建立WHERE子句。
wh_10 = curs.execute("SELECT prod_name, prod_price FROM Products WHERE vend_id IN ('DLL01', 'BRS01') ORDER BY prod_name;")

for row in wh_10:
    print(row)

wh_11 = curs.execute("SELECT prod_name FROM Products WHERE NOT vend_id = 'DLL01' ORDER BY prod_name;")

for row in wh_11:
    print(row)

wh_12 = curs.execute("SELECT prod_name FROM Products WHERE vend_id <> 'DLL01' ORDER BY prod_name;")

for row in wh_12:
    print(row)

conn.close()