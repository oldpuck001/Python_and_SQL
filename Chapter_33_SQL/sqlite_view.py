# SQLite_view.py

import sqlite3

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

curs.execute("CREATE VIEW ProductCustomers_6 AS SELECT cust_name, cust_contact, prod_id FROM Customers, Orders, OrderItems \
              WHERE Customers.cust_id = Orders.cust_id AND OrderItems.order_num = Orders.order_num;")

vi_1 = curs.execute("SELECT * FROM ProductCustomers_6;")

for row in vi_1:
    print(row)

vi_2 = curs.execute("SELECT cust_name, cust_contact FROM ProductCustomers_6 WHERE prod_id = 'RGAN01';")

for row in vi_2:
    print(row)

# 用视图重新格式化检索出的数据
curs.execute("CREATE VIEW VendorLocations_6 AS SELECT RTRIM(vend_name) || ' (' || RTRIM(vend_country) || ')' AS vend_title FROM Vendors;")

vi_3 = curs.execute("SELECT * FROM VendorLocations_6;")

for row in vi_3:
    print(row)

# 用视图过滤不想要的数据
curs.execute("CREATE VIEW CustomerEMailList_6 AS SELECT cust_id, cust_name, cust_email FROM Customers WHERE cust_email IS NOT NULL;")

vi_4 = curs.execute("SELECT * FROM CustomerEMailList_6;")

for row in vi_4:
    print(row)

# 使用视图与计算字段
curs.execute("CREATE VIEW OrderItemsExpanded AS \
              SELECT order_num, prod_id, quantity, item_price, quantity*item_price AS expanded_price FROM OrderItems;")

vi_5 = curs.execute('SELECT * FROM OrderItemsExpanded WHERE order_num = 20008;')

for row in vi_5:
    print(row)

conn.close()