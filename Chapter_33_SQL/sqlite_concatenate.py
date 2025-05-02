# SQLite_concatenate.py

import sqlite3

conn = sqlite3.connect('Chapter_33_SQL/tysql.sqlite')

curs = conn.cursor()

con_1 = curs.execute("SELECT vend_name || ' (' || vend_country || ')' FROM Vendors ORDER BY vend_name;")

for row in con_1:
    print(row[0])

# 许多数据库（不是所有）保存填充为列宽的文本值，而实际上你要的结果不需要这些空格。为正确返回格式化的数据，必须去掉这些空格。
# LTRIM()（去掉字符串左边的空格）以及 TRIM()（去掉字符串左右两边的空格）。
con_2 = curs.execute("SELECT RTRIM(vend_name) || ' (' || RTRIM(vend_country) || ')' FROM Vendors ORDER BY vend_name;")

for row in con_2:
    print(row[0])

con_3 = curs.execute("SELECT RTRIM(vend_name) || ' (' || RTRIM(vend_country) || ')' AS vend_title FROM Vendors ORDER BY vend_name;")

for row in con_3:
    print(row[0])

con_4 = curs.execute("SELECT vend_name, UPPER(vend_name) AS vend_name_upcase FROM Vendors ORDER BY vend_name;")

for row in con_4:
    print(row)

'''
函数                                     说明
LEFT()（或使用子字符串函数）                返回字符串左边的字符
LENGTH()（也使用DATALENGTH()或LEN()）     返回字符串的长度
LOWER()（Access使用LCASE()）             将字符串转换为小写
LTRIM()                                 去掉字符串左边的空格
RIGHT()（或使用子字符串函数）               返回字符串右边的字符
RTRIM()                                 去掉字符串右边的空格
SOUNDEX()                               返回字符串的SOUNDEX值
UPPER()（Access使用UCASE()）             将字符串转换为大写
'''
# 如果在创建SQLite时使用了SQLITE_SOUNDEX编译时选项，那么SOUNDEX()在SQLite中就可用。因为SQLITE_SOUNDEX不是默认的编译时选项，所以多数SQLite实现不支持SOUNDEX()。

con_5 = curs.execute("SELECT order_num FROM Orders WHERE strftime('%Y', order_date) = '2012';")

for row in con_5:
    print(row)

'''
常用数值处理函数
函数     说明
ABS()   返回一个数的绝对值
COS()   返回一个角度的余弦
EXP()   返回一个数的指数值
PI()    返回圆周率
SIN()   返回一个角度的正弦
SQRT()  返回一个数的平方根
TAN()   返回一个角度的正切
'''

conn.close()