# SQLite_update.py

import sqlite3

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

# SET命令用来将新值赋给被更新的列。
curs.execute("UPDATE Customers SET cust_email = 'kim@thetoystore.com' WHERE cust_id = '1000000005';")

ins_1 = curs.execute('SELECT * FROM Customers;')

for row in ins_1:
    print(row)

# UPDATE语句以WHERE子句结束，它告诉DBMS更新哪一行。没有WHERE子句，DBMS将会用这个电子邮件地址更新Customers表中的所有行，这不是我们希望的。
curs.execute("UPDATE Customers SET cust_contact = 'Sam Roberts', cust_email = 'sam@toyland.com' WHERE cust_id = '1000000006';")

ins_2 = curs.execute('SELECT * FROM Customers;')

for row in ins_2:
    print(row)

# NULL与保存空字符串很不同（空字符串用''表示，是一个值），而NULL表示没有值。
curs.execute("UPDATE Customers SET cust_email = NULL WHERE cust_id = '1000000005';")

ins_3 = curs.execute('SELECT * FROM Customers;')

for row in ins_3:
    print(row)

curs.execute("DELETE FROM Customers WHERE cust_id = '1000000006';")

ins_4 = curs.execute('SELECT * FROM Customers;')

for row in ins_4:
    print(row)

'''
简单联结两个表只需要这两个表中的常用字段。也可以让DBMS通过使用外键来严格实施关系（这些定义在附录 A 中）。
存在外键时，DBMS使用它们实施引用完整性。例如要向Products表中插入一个新产品，DBMS不允许通过未知的供应商id插入它，因为vend_id列是作为外键连接到
Vendors表的。那么，这与DELETE有什么关系呢？使用外键确保引用完整性的一个好处是，DBMS通常可以防止删除某个关系需要用到的行。
例如，要从Products表中删除一个产品，而这个产品用在OrderItems的已有订单中，那么DELETE语句将抛出错误并中止。
这是总要定义外键的另一个理由。
'''

# DELETE不需要列名或通配符。DELETE删除整行而不是删除列。要删除指定的列，请使用UPDATE语句。

# DELETE语句从表中删除行，甚至是删除表中所有行。但是，DELETE不删除表本身。

# 如果想从表中删除所有行，不要使用DELETE。可使用TRUNCATE TABLE语句，它完成相同的工作，而速度更快（因为不记录数据的变动）。

# 在UPDATE或DELETE语句使用WHERE子句前，应该先用SELECT进行测试，保证它过滤的是正确的记录，以防编写的WHERE子句不正确。

conn.close()