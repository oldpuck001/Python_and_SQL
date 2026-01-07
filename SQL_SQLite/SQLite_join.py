# SQLite_join.py

import sqlite3

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

# 联结類型：内联结（inner join，也稱為等值联结（equijoin），基于两个表之间的相等测试。）、自联结（self-join）、自然联结（natural join）和外联结（outer join）。

# 在联结两个表时，实际要做的是将第一个表中的每一行与第二个表中的每一行配对。WHERE子句作为过滤条件，只包含那些匹配给定条件（这里是联结条件）的行。
# 没有WHERE子句，第一个表中的每一行将与第二个表中的每一行配对，而不管它们逻辑上是否能配在一起。
# 要保证所有联结都有WHERE子句，否则将返回比想要的数据多得多的数据。同理，要保证WHERE子句的正确性。不正确的过滤条件会导致返回不正确的数据。
jo_1 = curs.execute("SELECT vend_name, prod_name, prod_price FROM Vendors, Products WHERE Vendors.vend_id = Products.vend_id;")

for row in jo_1:
    print(row)

# INNER JOIN指定的部分FROM子句。在使用这种语法时，联结条件用特定的ON子句而不是WHERE子句给出。传递给ON的实际条件与传递给WHERE的相同。
jo_2 = curs.execute("SELECT vend_name, prod_name, prod_price FROM Vendors INNER JOIN Products ON Vendors.vend_id = Products.vend_id;")

for row in jo_2:
    print(row)

jo_3 = curs.execute("SELECT prod_name, vend_name, prod_price, quantity FROM OrderItems, Products, Vendors \
                    WHERE Products.vend_id = Vendors.vend_id AND OrderItems.prod_id = Products.prod_id AND order_num = 20007;")

for row in jo_3:
    print(row)

jo_4 = curs.execute("SELECT cust_name, cust_contact FROM Customers WHERE cust_id IN (SELECT cust_id FROM Orders \
                    WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01'));")

for row in jo_4:
    print(row)

jo_4 = curs.execute("SELECT cust_name, cust_contact FROM Customers, Orders, OrderItems \
                    WHERE Customers.cust_id = Orders.cust_id AND OrderItems.order_num = Orders.order_num AND prod_id = 'RGAN01';")

for row in jo_4:
    print(row)

jo_5 = curs.execute("SELECT cust_name, cust_contact FROM Customers AS C, Orders AS O, OrderItems AS OI \
                    WHERE C.cust_id = O.cust_id AND OI.order_num = O.order_num AND prod_id = 'RGAN01';")

for row in jo_5:
    print(row)

# 自联结通常作为外部语句，用来替代从相同表中检索数据的使用子查询语句。虽然最终的结果是相同的，但许多DBMS处理联结远比处理子查询快得多。
# 应该试一下两种方法，以确定哪一种的性能更好。

jo_6 = curs.execute("SELECT cust_id, cust_name, cust_contact FROM Customers \
                    WHERE cust_name = (SELECT cust_name FROM Customers WHERE cust_contact = 'Jim Jones');")

for row in jo_6:
    print(row)

jo_6 = curs.execute("SELECT c1.cust_id, c1.cust_name, c1.cust_contact FROM Customers AS c1, Customers AS c2 \
                    WHERE c1.cust_name = c2.cust_name AND c2.cust_contact = 'Jim Jones';")

for row in jo_6:
    print(row)

jo_7 = curs.execute("SELECT C.*, O.order_num, O.order_date, OI.prod_id, OI.quantity, OI.item_price \
                    FROM Customers AS C, Orders AS O, OrderItems AS OI \
                    WHERE C.cust_id = O.cust_id AND OI.order_num = O.order_num AND prod_id = 'RGAN01';")

for row in jo_7:
    print(row)

# 事实上，很可能永远都不会用到不是自然联结的内联结。

# 联结包含了那些在相关表中没有关联行的行。这种联结称为外联结。

# 在使用OUTER JOIN语法时，必须使用RIGHT或LEFT关键字指定包括其所有行的表（RIGHT指出的是OUTER JOIN右边的表，而LEFT指出的是OUTER JOIN左边的表）。
# SQLite支持LEFT OUTER JOIN，但不支持RIGHT OUTER JOIN。SQLite不支持全外聯結FULL OUTER JOIN语法。
jo_8 = curs.execute("SELECT Customers.cust_id, Orders.order_num FROM Customers LEFT OUTER JOIN Orders ON Customers.cust_id = Orders.cust_id;")

for row in jo_8:
    print(row)

jo_9 = curs.execute("SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord FROM Customers INNER JOIN Orders \
                    ON Customers.cust_id = Orders.cust_id GROUP BY Customers.cust_id;")

for row in jo_9:
    print(row)

jo_10 = curs.execute("SELECT Customers.cust_id, COUNT(Orders.order_num) AS num_ord FROM Customers LEFT OUTER JOIN Orders \
                    ON Customers.cust_id = Orders.cust_id GROUP BY Customers.cust_id;")

for row in jo_10:
    print(row)

'''
联结及其使用的要点:
注意所使用的联结类型。一般我们使用内联结，但使用外联结也有效。
关于确切的联结语法，应该查看具体的文档，看相应的DBMS支持何种语法（大多数DBMS使用这两课中 述的某种语法）。
保证使用正确的联结条件（不管采用哪种语法），否则会返回不正确的数据。
应该总是供联结条件，否则会得出笛卡儿积。
在一个联结中可以包含多个表，甚至可以对每个联结采用不同的联结类型。虽然这样做是合法的，一般也很有用，但应该在一起测试它们前分别测试每个联结。这会使故障排除更为简单。
'''

conn.close()