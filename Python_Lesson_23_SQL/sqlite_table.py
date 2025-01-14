# sqlite_table.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

'''
利用CREATE TABLE创建表，必须给出下列信息：
新表的名字，在关键字CREATE TABLE之后给出；
表列的名字和定义，用逗号分隔；
有的DBMS还要求指定表的位置。
'''

# NULL为默认设置，如果不指定NOT NULL，就认为指定的是NULL。
curs.execute("CREATE TABLE Products_3 (prod_id CHAR(10) NOT NULL, vend_id CHAR(10) NOT NULL, \
              prod_name CHAR(254) NOT NULL, prod_price DECIMAL(8,2) NOT NULL, prod_desc VARCHAR(1000) NULL );")

cr_1 = curs.execute('SELECT * FROM Products_3;')

for row in cr_1:
    print(row)

'''
不要把NULL值与空字符串相混淆。NULL值是没有值，不是空字符串。如果指定''（两个单引号，其间没有字符），这在NOT NULL列中是允许的。
空字符串是一个有效的值，它不是无值。NULL值用关键字NULL而不是空字符串指定。
'''

# 默认值在CREATE TABLE语句的列定义中用关键字DEFAULT指定。
curs.execute("CREATE TABLE OrderItems_1 (order_num INTEGER NOT NULL, order_item INTEGER NOT NULL, \
              prod_id CHAR(10) NOT NULL, quantity INTEGER NOT NULL DEFAULT 1, item_price DECIMAL(8,2) NOT NULL);")

cr_2 = curs.execute('SELECT * FROM OrderItems_1;')

for row in cr_2:
    print(row)

# 默认值经常用于日期或时间戳列。例如，通过指定引用系统日期的函数或变量，将系统日期用作默认日期。SQLite中使用：date('now')

'''
使用ALTER TABLE时需要考虑的事情。
理想情况下，不要在表中包含数据时对其进行更新。应该在表的设计过程中充分考虑未来可能的需求，避免今后对表的结构做大改动。
所有的DBMS都允许给现有的表增加列，不过对所增加列的数据类型（以及NULL和DEFAULT的使用）有所限制。
许多DBMS不允许删除或更改表中的列。
多数DBMS允许重新命名表中的列。
许多DBMS限制对已经填有数据的列进行更改，对未填有数据的列几乎没有限制。
'''

# SQLite对使用ALTER TABLE执行的操作有所限制。最重要的一个限制是，它不支持使用ALTER TABLE定义主键和外键，这些必须在最初创建表时指定。
curs.execute("ALTER TABLE Vendors ADD vend_phone CHAR(20);")

cr_3 = curs.execute('SELECT * FROM Vendors;')

for row in cr_3:
    print(row)

curs.execute("ALTER TABLE Vendors DROP COLUMN vend_phone;")

cr_4 = curs.execute('SELECT * FROM Vendors;')

for row in cr_4:
    print(row)

'''
复杂的表结构更改一般需要手动删除过程，它涉及以下步骤：
1. 用新的列布局创建一个新表；
2. 使用INSERT SELECT语句从旧表复制数据到新表。有必要的话，可以使用转换函数和计算字段；
3. 检验包含所需数据的新表；
4. 重命名旧表（如果确定，可以删除它）；
5. 用旧表原来的名字重命名新表；
6. 根据需要，重新创建触发器、存储过程、索引和外键。
'''

'''
使用ALTER TABLE要极为小心，应该在进行改动前做完整的备份（模式和数据的备份）。数据库表的更改不能撤销，如果增加了不需要的列，也许无法删除它们。
类似地，如果删除了不应该删除的列，可能会丢失该列中的所有数据。
'''

# 删除表没有确认，也不能撤销，执行这条语句将永久删除该表。
curs.execute("DROP TABLE CustCopy;")

'''
使用关系规则防止意外删除
许多DBMS允许强制实施有关规则，防止删除与其他表相关联的表。
在实施这些规则时，如果对某个表发布一条DROP TABLE语句，且该表是某个关系的组成部分，则DBMS将阻止这条语句执行，直到该关系被删除为止。
如果允许，应该启用这些选项，它能防止意外删除有用的表。
'''

# SQLite用户使用ALTER TABLE语句重命名表。

conn.close()