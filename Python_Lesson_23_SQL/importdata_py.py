# importdata.py

import sqlite3

def convert(value):
    # 在示例txt文件中，每行都是一條數就記錄，字段之間用脱字符（^）分隔。數字字段直接包含數字，而文本字段用兩個波浪字符（~）將其字符串括起
    # 例如：~07276~^~HORMEL SPAM ... PORK W/ HAM MINCED CND~^ ... ^~1 serving~^^~~^0
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value='0'
    return float(value)

# 創建連結
conn = sqlite3.connect('food.db')

# 獲取游標
curs = conn.cursor()

# 調用curs.execute執行一條SQL INSERT語句，將字段中的值插入數據庫中
# 也可使用curs.executemany，並向它提供一個列表（其中包含從數據文件中提取的所有行）
curs.execute('''
CREATE TABLE food (

id      TEXT PRIMARY KEY,
desc    TEXT,
water   FLOAT,
kcal    FLOAT,
protein FLOAT,
fat     FLOAT,
ash     FLOAT,
carbs   FLOAT,
fiber   FLOAT,
sugar   FLOAT
)
''')

# 這裡使用的參數風格為qmark，即使用問號來標記字段
query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)'
field_count = 10
for line in open('ABBREV.txt'):
    fields = line.split('^')
    vals = [convert(f) for f in fields[:field_count]]
    curs.execute(query, vals)

# 
conn.commit()

# 關閉連結
conn.close()