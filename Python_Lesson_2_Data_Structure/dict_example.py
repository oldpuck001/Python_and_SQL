# dict_example.py

phonebook = {'Alice': '2341', 'Beth':'9102','Cecil':'3258'}
empty_dict = {}

print(empty_dict)

# 字典函數：
# 從键-值对、映射或關鍵字參數創建字典
items = [('name', 'Gumby'), ('age', 42)]
a_dict = dict(items)
print(a_dict)
print(a_dict['name'])

# 也可使用一個映射實參來調用它，這將創建一個字典，其中包含指定映射中的所有項。
b_dict = dict(name = 'Gumby', age = 42)
print(b_dict)

# 從映射創建字典時，如果該映射也是字典，可不使用函數dict，而是使用字典方法copy。
c_dict = phonebook.copy()
print(phonebook)
print(c_dict)
c_dict['Alice'] = '8848'
print(phonebook)
print(c_dict)
# 返回一個新字典，其包含的鍵值對與原來的字典相同（這個方法執行的是淺複製，因為值本身是原件，而非副本）.
# 當替換副本中的值時，原件不受影響。
# 如果修改副本中的值（就地修改而不是替換），原件也將發生變化，因為原件指向的也是被修改的值。
# 淺複製替換附件不影響原件，修改副本影響原件。

# fromkeys方法創建一個新字典，其中包含指定的鍵，且每個鍵對應的值都是None。如果不想使用默認值None，可提供特定的值。

d_dict = dict.fromkeys(['name','age'])
print(d_dict)
e_dict = dict.fromkeys(['name','age'],'(unknown)')
print(e_dict)

print(len(phonebook))
# len函数返回字典d包含的項（鍵值對）數。

print(phonebook['Beth'])
# 返回與鍵k相關聯的值。

phonebook['Beth'] = '4587'
print(phonebook['Beth'])
# 即便是字典中原本沒有的鍵，也可以給它賦值，這將在字典中創建一個新項。

d = 'Beth'
del phonebook[d]
print(phonebook)
# 刪除鍵為d的項。

if 'Cecil' in phonebook:
    print('Cecil is in phonebook.')
# 檢查字典phonebook是否包含鍵為'Cecil'的項。相比於檢查列表是否包含指定的值，檢查字典是否包含指定的鍵的效率更高。數據結構越大，效率差距就越大。

print(phonebook.get('Mike'))
print(phonebook.get('Jack', 'N/A'))
# 如果字典包含指定的鍵，get的作用將與普通字典查找相同;訪問不存在的鍵時，默認返回None，可以设置返回指定值。
# 访问不存在的键时，使用get方法、if语句、try/except语句的对比，请参考码农高天的视频：
# b站：https://www.bilibili.com/video/BV1MM411w7Te/?spm_id_from=333.337.search-card.all.click
# YouTube：https://www.youtube.com/watch?v=NjeiQY9aNW4&list=PLmDfTmp9rjCmZKR7NaS2GHwZlMW0VFt4C&index=5

phonebook.setdefault('Tom')
print(phonebook)
phonebook.setdefault('Lee', 'N/A')
print(phonebook)
# 如果指定的鍵存在，就返回其值，並保持字典不變。指定的鍵不存在時，setdefault返回指定的值並相應地更新字典。值的默認為None，可以设置指定值。

x = {'Tom': '3126', 'Lee': '9901'}
phonebook.update(x)
print(phonebook)
# update方法使用一個字典中的項來更新另一個字典。對於通過參數提供的字典，將其項添加到當前字典中。
# 如果當前字典包含鍵相同的項，就替換它。可像調用函數dict（類型構造函數）那樣調用方法update。
# 這意味著調用update時，可向它提供一個映射、一個由鍵值對組成的序列（或其他可迭代對象）或關鍵字參數。

phonebook.pop('Tom')
print(phonebook)
# pop方法用於獲取與指定鍵相關聯的值，並將該鍵值對從字典中刪除。

phonebook.popitem()
print(phonebook)
key, value = phonebook.popitem()
print(key)
print(value)

# popitem方法隨機彈出一個字典項並刪除。如果要以高效地方式逐個刪除並處理所有字典項，這可能很有用，因為這樣無需先獲取鍵列表。

dict_items = phonebook.items()
print(dict_items)
# items方法返回一個包含所有字典項的列表（返回值屬於一種名為字典視圖的特殊類型。
# 字典視圖可用於迭代，還可確定其長度以及對其執行成員資格檢查。
# 視圖的一個優點是不復制，它們始終是底層字典的反映，即便修改了底層字典亦如此。），其中每個元素都為(key, value)的形式。
# 字典項在列表中的排列順序不確定。

dict_keys = phonebook.keys()
print(dict_keys)
# keys方法返回一個字典視圖，其中包含指定字典中的鍵。

dict_vales = phonebook.values()
print(dict_vales)
# values方法返回由字典的值組成的字典視圖。不同於方法keys，方法values返回的視圖可能包含重複的值。

phonebook.clear()
print(phonebook)
# clear方法刪除所有的字典項，這種操作是就地執行的（就像list、sort一樣），因此什麼都不返回（或者說返回None）。
