# SQLite_union.py

import sqlite3

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

# SQL也允许执行多个查询（多条SELECT语句），并将结果作为一个查询结果集返回。这些组合查询通常称为并（union）或复合查询（compound query）。

un_1 = curs.execute("SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL','IN','MI') UNION \
                     SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All';")

for row in un_1:
    print(row)

un_2 = curs.execute("SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL','IN','MI') OR cust_name = 'Fun4All';")

for row in un_2:
    print(row)

'''
在进行组合时需要注意几条规则:
UNION必须由两条或两条以上的SELECT语句组成，语句之间用关键字UNION分隔（因此，如果组合四条SELECT语句，将要使用三个UNION关键字）。
UNION中的每个查询必须包含相同的列、表达式或聚集函数（不过，各个列不需要以相同的次序列出）。
列数据类型必须兼容：类型不必完全相同，但必须是DBMS可以隐含转换的类型（例如，不同的数值类型或不同的日期类型）。
'''

# 使用UNION时，重复的行会被自动取消。如果想返回所有的匹配行，可使用UNION ALL而不是UNION。使用UNION ALL，DBMS不取消重复的行。
# UNION ALL为UNION的一种形式，它完成WHERE子句完成不了的工作。如果确实需要每个条件的匹配行全部出现（包括重复行），就必须使用UNION ALL，而不是WHERE。
un_3 = curs.execute("SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL','IN','MI') UNION ALL \
                     SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All';")

for row in un_3:
    print(row)

# 在用UNION组合查询时，只能使用一条ORDER BY子句，它必须位于最后一条SELECT语句之后。不允许使用多条ORDER BY子句。
un_4 = curs.execute("SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_state IN ('IL','IN','MI') UNION \
                    SELECT cust_name, cust_contact, cust_email FROM Customers WHERE cust_name = 'Fun4All' \
                    ORDER BY cust_name, cust_contact;")

for row in un_4:
    print(row)

# UNION在需要组合多个表的数据时也很有用，即使是有不匹配列名的表，在这种情况下，可以将UNION与别名组合，检索一个结果集。
# 利用UNION，可以把多条查询的结果作为一条组合查询返回，不管结果中有无重复。使用UNION可极大地简化复杂的WHERE子句，简化从多个表中检索数据的工作。

conn.close()