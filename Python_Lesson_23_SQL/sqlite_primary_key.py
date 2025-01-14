# sqlite_primary_key.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

'''
表中任意列只要满足以下条件，都可以用于主键：
任意两行的主键值都不相同。
每行都具有一个主键值（即列中不允许NULL值）。
包含主键值的列从不修改或更新。（大多数DBMS不允许这么做，但如果你使用的DBMS允许这样做，好吧，千万别！）
主键值不能重用。如果从表中删除某一行，其主键值不分配给新行。
'''

# SQLite 不允许使用 ALTER TABLE 定义键，要求在初始的 CREATE TABLE 语句中定义它们。
curs.execute('CREATE TABLE Vendors_4 (vend_id CHAR(10) NOT NULL PRIMARY KEY, vend_name CHAR(50) NOT NULL, \
              vend_address CHAR(50) NULL, vend_city CHAR(50) NULL, vend_state CHAR(5) NULL, vend_zip CHAR(10) NULL, \
              vend_country CHAR(50) NULL);')

pk_1 = curs.execute('SELECT * FROM Vendors_4')

for row in pk_1:
    print(row)

# 外鍵
curs.execute('CREATE TABLE Orders_4 (order_num INTEGER NOT NULL PRIMARY KEY, order_date DATETIME NOT NULL, \
              cust_id CHAR(10) NOT NULL REFERENCES Customers(cust_id));')

pk_2 = curs.execute('SELECT * FROM Orders_4')

for row in pk_2:
    print(row)

'''
外键有助防止意外删除
除帮助保证引用完整性外，外键还有另一个重要作用。在定义外键后，DBMS不允许删除在另一个表中具有关联行的行。例如，不能删除关联订单的顾客。
删除该顾客的唯一方法是首先删除相关的订单（这表示还要删除相关的订单项）。由于需要一系列的删除，因而利用外键可以防止意外删除数据。
有的DBMS支持称为级联删除（cascading delete）的特性。如果启用，该特性在从一个表中删除行时删除所有相关的数据。\
例如，如果启用级联删除并且从Customers表中删除某个顾客，则任何关联的订单行也会被自动删除。
'''

'''
唯一约束用来保证一列（或一组列）中的数据是唯一的。它们类似于主键，但存在以下重要区别。
表可包含多个唯一约束，但每个表只允许一个主键。
唯一约束列可包含 NULL 值。
唯一约束列可修改或更新。
唯一约束列的值可重复使用。
与主键不一样，唯一约束不能用来定义外键。
唯一约束的语法类似于其他约束的语法。唯一约束既可以用UNIQUE关键字在表定义中定义，也可以用单独的CONSTRAINT定义。
'''

curs.execute('CREATE TABLE OrderItems_4 (order_num INTEGER NOT NULL, order_item INTEGER NOT NULL, \
              prod_id CHAR(10) NOT NULL, quantity INTEGER NOT NULL CHECK (quantity > 0), item_price MONEY NOT NULL);')

pk_3 = curs.execute('SELECT * FROM OrderItems_4')

for row in pk_3:
    print(row)

'''
SQLite支援CHECK約束，但只能在創建表格時使用。例如：
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    gender TEXT,
    CHECK (gender IN ('M', 'F'))
);
'''

'''
有的DBMS允许用户定义自己的数据类型。它们是定义检查约束（或其他约束）的基本简单数据类型。
例如，你可以定义自己的名为gender的数据类型，它是单字符的文本数据类型，带限制其值为M或F（对于未知值或许还允许 NULL）的检查约束。
然后，可以将此数据类型用于表的定义。定制数据类型的优点是只需施加约束一次（在数据类型定义中），而每当使用该数据类型时，都会自动应用这些约束。
'''

'''
触发器是特殊的存储过程，它在特定的数据库活动发生时自动执行。触发器可以与特定表上的INSERT、UPDATE和DELETE操作（或组合）相关联。
与存储过程不一样（存储过程只是简单的存储SQL语句），触发器与单个的表相关联。与Orders表上的INSERT操作相关联的触发器只在Orders表中插入行时执行。
类似地，Customers表上的INSERT和UPDATE操作的触发器只在表上出现这些操作时执行。
触发器内的代码具有以下数据的访问权：
INSERT操作中的所有新数据；
UPDATE操作中的所有新数据和旧数据；
DELETE操作中删除的数据。
根据所使用的DBMS的不同，触发器可在特定操作执行之前或之后执行。
'''

# 一般来说，约束的处理比触发器快，因此在可能的时候，应该尽量使用约束。

conn.close()