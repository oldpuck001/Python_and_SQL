# example_2.py

# 自定義類別

# 參數是整數
num = 123
print('num = 123')
print(type(num))
print('repr(num)')
print(repr(num))
print(type(repr(num)))
print('\n')

# 參數是浮點數
float_num = 3.14
print('float_num = 3.14')
print(type(float_num))
print('repr(float_num)')
print(repr(float_num))
print(type(repr(float_num)))
print('\n')

# 字串
text = "Hello, World!"
print('text = "Hello, World!"')
print(type(text))
print('repr(text)')
print(repr(text))
print(type(repr(text)))
print('\n')

# 使用自定義類別，如果你定義了一個類別，通常你可以覆寫 `__repr__` 方法來指定 `repr()` 的行為。
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"
# 建立物件
p = Person("Alice", 30)
print(repr(p))
print('\n')

# 列表
my_list = [1, 2, 3]
print('my_list = [1, 2, 3]')
print(type(my_list))
print('repr(my_list)')
print(repr(my_list))
print(type(repr(my_list)))
print('\n')

# 字典
my_dict = {'name': 'Alice', 'age': 30}
print('my_dict = {\'name\': \'Alice\', \'age\': 30}')
print(type(my_dict))
print('repr(my_dict)')
print(repr(my_dict))
print(type(repr(my_dict)))
print('\n')

# 結合 eval() 使用
my_list = [1, 2, 3]
list_repr = repr(my_list)  # list_repr 為 '[1, 2, 3]'
# 使用 eval 重建列表
reconstructed_list = eval(list_repr)
print(reconstructed_list)  # 輸出: [1, 2, 3]