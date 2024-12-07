# DataFrame_example.py

# pd.DataFrame
# df.info()
# df.index
# df.index.name
# df.reset_index
# df.set_index
# df.reindex
# df.sort_index
# df.sort_values
# df.columns
# df.columns.name
# df.rename
# df.drop
# df.transpose

import pandas as pd

columns = ['name', 'No.', 'country', 'score', 'job']

index=[1001, 1000, 1002, 1003]

data_1 = [['Mike', 1, 'Thailand', 80, 'teacher'],
          ['Yang', 2, 'China', 77, 'student'],
          ['Tom', 3, 'England', 85, 'student'],
          ['Losa', 4, 'Japan', 90, 'accounting']]

data_2 = {'name': ['Mike', 'Yang', 'Tom', 'Losa'],
          'No.': [1, 2, 3, 4],
          'country': ['Thailand', 'China', 'England', 'Japan'],
          'score': [80, 77, 85, 90],
          'job': ['teacher', 'student', 'student', 'accounting']
        }

# 创建一个空白的 DataFrame
empty_df = pd.DataFrame()

# 创建带有列名的空白 DataFrame
columns = ['Column1', 'Column2', 'Column3']
empty_df_with_columns = pd.DataFrame(columns=columns)

# 使用列表或字典構造DataFrame
df = pd.DataFrame(data=data_1, columns=columns, index=index)
df_dict = pd.DataFrame(data=data_2, index=index)

print(df)
print(df_dict)

#  info 方可以得 DataFrame 的本，的是数据数和的数据型
print(df.info())

# index是DataFrame數據結構的索引，和数据库的不同，DataFrame 的索引可以重复
print(df.index)

# 給索引命名
df.index.name = 'user_id'
print(df)

# 調用 DataFrame 的方法時，返回的是副本，所以原來的 DataFrame 沒有任何變化.
# 可以使用 df = df.reset_index() 的方法將返回值賦給原來的變量。

# reset_index，可以將索引變成普通的列
df_reset_index = df.reset_index()
print(df_reset_index)

# set_index，可以將一個普通列設置成一個新的索引，索引可以是多級的
df_set_index_1 = df.reset_index().set_index('name')
print(df_set_index_1)
df_set_index_2 = df.reset_index().set_index(['job', 'country'])
print(df_set_index_2)
df_set_index_3 = df_set_index_2.reset_index(level=0)
print(df_set_index_3)

# 這裡是鏈式方法調用（method chaining），執行順序從左到右，省去了寫中間值
df_method_chaining = df.reset_index().set_index('No.')
print(df_method_chaining)

# reindex 更新索引，這個方法會匹配所有新索引的行，無法匹配的行的索引會變為空值NaN
new_index = [999, 1000, 1001, 1004]
df_new_index = df.reindex(new_index)
print(df_new_index)

# sort_index 按索引排序
df_sort_index = df.sort_index()
print(df_sort_index)

# 按一列排序
# 按多列排序
df_sort_values_one = df.sort_values('score')
print(df_sort_values_one)

# 按多列排序
df_sort_values_more = df.sort_values(['job', 'score'])
print(df_sort_values_more)

# 獲取列的信息，構造DataFrame數據結構時，如過沒有提供列明，將會從0開始的數字為列編號
print(df.columns)

# 給索引列命名
df.columns.name = 'properties'
print(df)

# rename 給列重命名
df_rename = df.rename(columns={'name': 'First Name', 'No.': 'num'})
print(df_rename)

# drop 刪除列與刪除行
df_drop = df.drop(columns=["name", "country"], index=[1000, 1003])
print(df_drop)

# transpose 方法將 DataFrame 數據結構轉置
# df.transpose() 的縮寫
df_transpose = df.T
print(df_transpose)