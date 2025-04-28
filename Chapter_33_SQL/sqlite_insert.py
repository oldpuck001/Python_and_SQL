# sqlite_insert.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

curs.execute("INSERT INTO Customers VALUES('1000000006','Toy Land','123 Any Street','New York','NY','11111','USA', NULL, NULL);")

ins_1 = curs.execute('SELECT * FROM Customers;')

for row in ins_1:
    print(row)

# 不要使用没有明确给出列的 INSERT 语句。给出列能使 SQL 代码继续发挥作用，即使表结构发生了变化。
curs.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country, cust_contact, cust_email) \
              VALUES('1000000007', 'Toy Land', '123 Any Street', 'New York', 'NY', '11111', 'USA', NULL, NULL);")

ins_2 = curs.execute('SELECT * FROM Customers;')

for row in ins_2:
    print(row)

# 使用INSERT的推荐方法是明确给出表的列名。使用这种语法，还可以省略列，这表示可以只给某些列供值，给其他列不供值。
curs.execute("INSERT INTO Customers(cust_id, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country) \
              VALUES('1000000008','Toy Land','123 Any Street','New York','NY','11111','USA');")

ins_3 = curs.execute('SELECT * FROM Customers;')

for row in ins_3:
    print(row)

'''
省略的列必须满足以下某个条件。
该列定义为允许NULL值（无值或空值）。
在表定义中给出默认值。这表示如果不给出值，将使用默认值。
如果对表中不允许NULL值且没有默认值的列不给出值，DBMS将产生错误消息，并且相应的行插入不成功。


curs.execute("INSERT INTO Customers(cust_id, cust_contact, cust_email, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country) \
              SELECT cust_id, cust_contact, cust_email, cust_name, cust_address, cust_city, cust_state, cust_zip, cust_country FROM CustNew;")

ins_4 = curs.execute('SELECT * FROM Customers;')

for row in ins_4:
    print(row)
'''

# INSERT通常只插入一行。要插入多行，必须执行多个INSERT语句。INSERT SELECT是个例外，它可以用一条INSERT插入多行，不管SELECT语句返回多少行，都将被INSERT插入。

curs.execute('CREATE TABLE CustCopy AS SELECT * FROM Customers;')

ins_5 = curs.execute('SELECT * FROM CustCopy;')

for row in ins_5:
    print(row)

'''
在使用SELECT INTO时，需要知道一些事情：
任何SELECT选项和子句都可以使用，包括WHERE和GROUP BY；
可利用联结从多个表插入数据；
不管从多少个表中检索数据，数据都只能插入到一个表中。
'''

# SELECT INTO是试验新SQL语句前进行表复制的很好工具。先进行复制，可在复制的数据上测试SQL代码，而不会影响实际的数据。

conn.close()