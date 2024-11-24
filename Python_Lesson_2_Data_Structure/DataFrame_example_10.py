# DataFrame_example_10.py

import pandas as pd

# 并将绘图后端设置为Plotl
pd.options.plotting.backend = 'plotly'

# 以时间戳为索引可以让筛选数据更加简单

# pandas 为构造DatetimeIndex提供了date_range函数
# 它会接受一个开始日期、周期数或者结束日期、一个频率参数（freq='D'）
daily_index = pd.date_range('2020-02-28', periods=4, freq='D')
print(daily_index)
weekly_index = pd.date_range('2020-01-01', '2020-01-31', freq='W-SUN')
print(weekly_index)

# 通过weekly_index构造DatetimeIndex
df_data_range = pd.DataFrame(data=[21, 15, 33, 34], columns=['count'], index=weekly_index)
print(df_data_range)

# 在需要轉換為時間戳的列上执行to_datetime函数，並將結果重新賦值給該列
columns = ['date', 'name', 'No.', 'country', 'score', 'job']
index = [1001, 1000, 1002, 1003]
data = [['2022/12/04', 'Mike', 1, 'Thailand', 80, 'teacher'],
        ['2001/5/13', 'Yang', 2, 'China', 77, 'student'],
        ['1999/9/19', 'Tom', 3, 'England', 85, 'student'],
        ['1990/2/21', 'Losa', 4, 'Japan', 90, 'accounting']]
df_1 = pd.DataFrame(data, columns=columns, index=index)
print(df_1)
print(df_1.info())

df_1['date'] = pd.to_datetime(df_1['date'])
print(df_1)
print(df_1.info())

# astype方法轉換數據類型
df_1['score'] = df_1['score'].astype('float')
print(df_1)
print(df_1.info())

# 只需访问DatetimeIndex的一部分時，可以使用date、year、month、day等屬性
print(df_1['date'].dt.date)
print(df_1['date'].dt.year)
print(df_1['date'].dt.month)
print(df_1['date'].dt.day)


# 通过parse_dates参数告诉read_csv这一列包含时间戳
# parse_dates会接受一个列名列表或者索引作为参数
# dtype參數會在讀取的時候，轉換值的數據類型
file_path = '/Users/lei/Downloads/a.csv'
try:
    df_2 = pd.read_csv(file_path, index_col='date', parse_dates=['date'], dtype={'score': float})
    print(df_2)
    print(df_2.info())
except:
    pass

# 在处理时序时，开始分析之前最好先排序
df_2 = df_2.sort_index()
print(df_2)

# 只需访问DatetimeIndex的一部分時，可以使用date、year、month、day等屬性
print(df_2.index.date)
print(df_2.index.year)
print(df_2.index.month)
print(df_2.index.day)

# 筛选DatetimeInde
print(df_2.loc['1999', 'score'])
df_chart = df_2.loc['1990-2':'2022-12', 'score'].plot()
df_chart.show()

# DateOffset方法可以為時間戳添加時間
df_3 = df_2.copy()
df_3.index = df_3.index + pd.DateOffset(hours=16)
print(df_3)

# tz_localize为时间戳添加時區,格林尼治标准时间（GMT）
df_3 = df_3.tz_localize('America/New_York')
print(df_3)

# tz_convert方法为时间戳添加時區，UTC协调世界时（Coordinated Universal Time）
# UTC 闭市时间的变化依赖于纽约夏令时（daylight saving time，DST）的生效情况
# 即一年中的夏令時與非夏令時日期，會相差一個小時
df_3 = df_3.tz_convert('UTC')
print(df_3)