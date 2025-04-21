# sqlite_subquery.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

sq_1 = curs.execute("SELECT cust_id FROM Orders WHERE order_num IN (SELECT order_num FROM OrderItems WHERE prod_id = 'RGAN01');")

for row in sq_1:
    print(row)

sq_2 = curs.execute("SELECT cust_name, cust_contact FROM Customers WHERE cust_id IN (SELECT cust_id FROM Orders \
                    WHERE order_num IN (SELECT order_num FROM OrderItems \
                    WHERE prod_id = 'RGAN01'));")

for row in sq_2:
    print(row)

sq_3 = curs.execute("SELECT cust_name, cust_state, (SELECT COUNT(*) FROM Orders \
                    WHERE Orders.cust_id = Customers.cust_id) AS orders FROM Customers ORDER BY cust_name;")

for row in sq_3:
    print(row)

conn.close()