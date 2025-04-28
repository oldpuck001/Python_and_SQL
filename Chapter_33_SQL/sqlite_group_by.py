# sqlite_group_by.py

import sqlite3

conn = sqlite3.connect('Python_Lesson_23_SQL/tysql.sqlite')

curs = conn.cursor()

gb_1 = curs.execute("SELECT vend_id, COUNT(*) AS num_prods FROM Products GROUP BY vend_id;")

for row in gb_1:
    print(row)

'''
GROUP BY子句可以包含任意数目的列，因而可以对分组进行嵌套，更细致地进行数据分组。
如果在GROUP BY子句中嵌套了分组，数据将在最后指定的分组上进行汇总。换句话说，在建立分组时，指定的所有列都一起计算（所以不能从个别的列取回数据）。
GROUP BY子句中列出的每一列都必须是检索列或有效的表达式（但不能是聚集函数）。如果在SELECT中使用表达式，则必须在GROUP BY子句中指定相同的表达式。不能使用别名。
大多数SQL实现不允许GROUP BY列带有长度可变的数据类型（如文本或备注型字段）。
除聚集计算语句外，SELECT语句中的每一列都必须在GROUP BY子句中给出。
如果分组列中包含具有NULL值的行，则NULL将作为一个分组返回。如果列中有多行NULL值，它们将分为一组。
GROUP BY子句必须出现在WHERE子句之后，ORDERBY子句之前。
'''

# WHERE过滤行，而HAVING过滤分组。HAVING支持所有WHERE操作符。
gb_2 = curs.execute("SELECT cust_id, COUNT(*) AS orders FROM Orders GROUP BY cust_id HAVING COUNT(*) >= 2;")

for row in gb_2:
    print(row)

# HAVING与WHERE非常类似，如果不指定GROUP BY，则大多数DBMS会同等对待它们。不过，你自己要能区分这一点。使用HAVING时应该结合GROUP BY子句，而WHERE子句用于标准的行级过滤。
gb_3 = curs.execute("SELECT vend_id, COUNT(*) AS num_prods FROM Products WHERE prod_price >= 4 GROUP BY vend_id HAVING COUNT(*) >= 2;")

for row in gb_3:
    print(row)

gb_4 = curs.execute("SELECT vend_id, COUNT(*) AS num_prods FROM Products GROUP BY vend_id HAVING COUNT(*) >= 2;")

for row in gb_4:
    print(row)

# 一般在使用GROUP BY子句时，应该也给出ORDER BY子句。这是保证数据正确排序的唯一方法。千万不要仅依赖GROUP BY排序数据。

gb_5 = curs.execute("SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING COUNT(*) >= 3;")

for row in gb_5:
    print(row)

gb_6 = curs.execute("SELECT order_num, COUNT(*) AS items FROM OrderItems GROUP BY order_num HAVING COUNT(*) >= 3 ORDER BY items, order_num;")

for row in gb_6:
    print(row)

'''
SELECT子句及其顺序
子句         说明               是否必须使用
SELECT      要返回的列或表达式    是
FROM        从中检索数据的表     仅在从表选择数据时使用
WHERE       行级过滤            否
GROUP BY    分组说明            仅在按组计算聚集时使用
HAVING      组级过滤            否
ORDER BY    输出排序顺序         否
'''

conn.close()