# example_2.py

# 檢查數據類型

def data_type_isinstance(data):

    if isinstance(data, str):
        data_type = 'str'
    elif isinstance(data, int):
        data_type = 'int'
    elif isinstance(data, float):
        data_type = 'float'
    else:
        data_type = 'other'

    return data_type

def data_type_type(data):

    if type(data) == str:
        data_type = 'str'
    elif type(data) == int:
        data_type = 'int'
    elif type(data) == float:
        data_type = 'float'
    else:
        data_type = 'other'

    return data_type

a = 3
print(a, type(a))
print(data_type_isinstance(a))
print(data_type_type(a))

b = 3.14
print(b, type(b))
print(data_type_isinstance(b))
print(data_type_type(b))

c = '3.14'
print(c, type(c))
print(data_type_isinstance(c))
print(data_type_type(c))

d = 'abc'
print(d, type(d))
print(data_type_isinstance(d))
print(data_type_type(d))