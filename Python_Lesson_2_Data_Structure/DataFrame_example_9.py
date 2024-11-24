# DataFrame_example_9.py

# 繪圖

import pandas as pd

'''
pandas图表类型
类型         描述
line        折线图，使用 df.plot() 时的默认选项
bar         垂直柱状图
barh        水平柱状图
hist        矩形图
box         箱形图
kde         密度图，可通过density启用
area        面积图
scatter     散点图
hexbin      六边形图
pie         饼状图
'''

data = [[3254.220271, 96398.309860, 16845.951895, 41671.684909],
        [87316.022433, 45183.397951, 15460.819455, 50951.465770],
        [51458.760432, 3821.139360, 77793.393899, 98915.952421],
        [64933.848496, 7600.277035, 55001.831706, 86248.512650]]

data = pd.DataFrame(data=data, index=["Q1", "Q2", "Q3", "Q4"], columns=["East", "West", "North", "South"])
data.index.name = "Quarters"
data.columns.name = "Region"
print(data)

# 将绘图后端设置为Plotly
pd.options.plotting.backend = 'plotly'

p_1 = data.plot()
p_1.show()
p_2 = data.plot.bar(barmode="group")
p_2.show()