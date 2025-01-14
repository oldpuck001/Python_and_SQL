# sqlite_like.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

# %表示任何字符出现任意次数
ob_1 = curs.execute("SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE 'Fish%';")

for row in ob_1:
    print(row)

ob_2 = curs.execute("SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '%bean bag%';")

for row in ob_2:
    print(row)

# 通配符%看起来像是可以匹配任何东西，但有个例外，这就是NULL。子句WHERE prod_name LIKE '%'不会匹配产品名称为NULL的行。

# 下划线（_）通配符的用途与%一样，但它只匹配单个字符，而不是多个字符。
ob_3 = curs.execute("SELECT prod_id, prod_name FROM Products WHERE prod_name LIKE '__ inch teddy bear';")

for row in ob_3:
    print(row)

conn.close()