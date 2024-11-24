# list_example

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
b_list = [16, 17, 18, 19, 20]
c_list = [None] * 3
d_list = ['a', 'b', 'c', 'd']
f_list = [22, 23, 24, 25]

print(a_list)
print(a_list[4:10])
print(a_list[4:10][2])
print(c_list)

# 切片的簡寫：如果切片結束於序列末尾，可以省略第二個索引。
print('切片的簡寫：')
print(a_list[-3:])
print(a_list[:3])
print(a_list[11:-4])
print(a_list[:])              # 切片整個序列的縮寫
print(a_list[-3:])            # 索引也可以使用負數。使用負數時，如果要包含最後一個元素，即-1索引位置的元素
print(a_list[3:10:3])          # 切片可以有步長
print(a_list[::-1])           # 有步長時，可以照常用簡寫，步長可以為正數或負數，不能為0。
print(a_list[8:3:-1])         # 步長為負數時，第一個索引必須比第二個索引大。

# 列表相加：+ 用加法運算符相加，不能拼接不同類型的序列。
print(a_list + c_list + d_list)

#列表的乘法：* 將序列與數x相乘時，將重複這個序列x次來創建一個新序列。
print(b_list * 2)

# 列表的成員資格檢查：in 要檢查特定的值是否包含在序列中，可以使用運算符in，包含返回True，不包含返回False。
if 'b' in d_list:
    print('b is in d_list.')

#修改列表（給元素賦值）：不能給不存在的元素賦值。
b_list[2] = 100
print(b_list) 

#刪除列表元素：del 列表的長度會相應減少。
del b_list[2]
print(b_list) 

#給列表切片賦值：使用切片賦值，即可將切片替換為長度與其不同的序列,也可在不替換原有元素的情況下插入新元素。 
d_list[2:] = list('ython')        # “替換”了一個空切片，相當於插入了一個序列。
print(d_list)
b_list[1:3] = []                  # 與del b_list[1:2]等效；可以執行步長不為1（乃至為負）的切片賦值。
print(b_list)
a_list[2:7:2]=[100, 100, 100]     # 與del b_list[1:2]等效；可以執行步長不為1（乃至為負）的切片賦值。
print(a_list)
b_list[1:1] = [17, 18, 19]                  # 使用切片賦值插入数据。
print(b_list)

# 列表函數：
# 將序列轉換為列表（創建列表），list可將任何序列（而不僅僅是字符串）作為list的參數。
print(list('Python'))       # list實際上是一個類，而不是函數。

print(len(a_list))          # 返回序列包含的元素個數。

print(min(a_list))          # 返回序列中最小的元素。

print(max(a_list))          # 返回序列中最大的元素。

# 列表方法：
b_list.append(21)
print(b_list)
# 將一個對象附加到列表末尾，直接修改舊列表，不會返回修改後的新列表。

b_list.extend(f_list)
print(b_list)
# extend，同時將多個值附加到列表末尾，可使用一個列表來擴展另一個列表。
# 與拼接的不同之處，拼接返回一個新序列，extend方法修改原序列。
# 為獲得與extend相同的效果，可將列表賦給切片 a[len(a):]=b或者a=a+b，但可讀性或效率不高。

print(a_list.count(5))
# count，計算指定的元素在列表中出現了多少次。

print(a_list.index(5))
# index，在列表中查找指定值第一次出現的索引，指定值查找不到時會出現異常。

b_list.insert(3, 'four')
print(b_list)
# insert，將一個對象插入列表。可使用切片賦值來獲得與insert一樣的效果。
# 切片賦值insert方法效果相同，但可讀性無法媲美。

g_list = a_list.copy()
print(g_list)
# copy，複製列表（關聯到a的副本），b=a.copy()類似於使用b=a[:]或b=list(a)，而不是b=a這樣關聯到a本身

print(b_list.pop())
print(b_list.pop(3))
# pop，從列表中刪除一個元素（默認為最後一個元素），並返回這一元素。pop是唯一即修改列表又返回一個非None值的列表方法。

d_list.remove('b')
print(d_list)
# remove，刪除第一個為指定值的元素，但無法刪除列表中其他為指定值的元素，而且也不返回任何值。
# remove是就地修改且不返回值的方法之一。不同於pop的是，它修改列表，但不返回任何值。

f_list.clear()
print(f_list)
#列表方法：clear，就地清空列表的內容，直接修改舊列表。類似於切片賦值語句lst[:]=[]

a_list.reverse()
print(a_list)
print(list(reversed(b_list)))
# reverse，按相反的順序排列列表中的元素，reverse修改列表，但不返回任何值。例如：x.reverse()
# reversed，返回一個按相反順序排列的迭代器，需要按相反的順序迭代序列時使用。可使用list將返回的對象轉換為列表。

a_list.sort()
print(a_list)
h_list = sorted(b_list)
print(h_list)

# sort，對列表就地排序。需要排序後的列表副本並保留原始列表不變時，正確的方法之一是先將y關聯到x的副本，再對y進行排序。
# 方法sort接受兩個可選參數：key和reverse。
# key：可將key設置為一個用於排序的函數。
# 不會直接使用這個函數來判斷一個元素是否比另一個元素小，而是使用它來為每個元素創建一個鍵，再根據這些鍵對元素進行排序。
# 例如x.sort(key=len) 根據長度對元素進行排序。很多情況下，將參數key設置為一個自定義函數很有用。
# reverse：設定為True時，反向排序。 x.sort(reverse=True)。
# 如果要將元素按相反的順序排列，可先使用sort（或sorted），再調用方法reverse，也可使用參數reverse。
# sorted，獲取排序後的列表的副本， 可用於任何可迭代的對象（比如所有序列），但總是返回一個列表。
# 函數sorted接受參數key和reverse，詳見sort函數。
# 如果要將元素按相反的順序排列，可先使用sort（或sorted），再調用方法reverse，也可使用參數reverse。