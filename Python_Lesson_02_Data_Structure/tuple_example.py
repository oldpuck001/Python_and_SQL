# tuple_example.py

a_tuple = (1, 2, 3)
b_tuple = ('a', 'b', 'c', 'd')
c_tuple = ()
d_tuple = (42,) 

print(a_tuple)
print(b_tuple)
print(c_tuple)
print(d_tuple)

e_tuple = tuple([1,2,3])
print(e_tuple)
f_tuple = tuple('abc')
print(f_tuple)
g_list = tuple((1,2,3))
print(g_list)
# tuple函數將序列轉換為元組（創建元組），tuple可將任何序列（而不僅僅是字符串）作為tuple的參數。tuple實際不是函數，是一個類。

print(b_tuple[1])
# 元组的索引(indexing),第一個元素的索引是0；最後一個元素的索引是 -1

print(b_tuple[1: 2])
# 元組的切片(slicing),第一個索引是包含的第一個元素的編號，第二個索引是切片後餘下的第一個元素的編號。
# 元组的切片也是元组，就像列表的切片也是列表一样。

h_tuple = a_tuple + b_tuple
print(h_tuple)
# 元組相加+，用加法運算符相加。

i_tuple = b_tuple * 3
print(i_tuple)
j_tuple = (42,) * 5
print(j_tuple)
k_tuple = (None,) * 3
print(k_tuple)
# 元組的乘法*，將元組與數x相乘時，將重複這個元組x次來創建一個新元組。

if 'b' in b_tuple:
    print('b is in b_tuple')
#元組的成員資格檢查：in 要檢查特定的值是否包含在元組中，可以使用運算符in，包含返回True，不包含返回False。

#元組函數：
print(len(a_tuple))
# len函數返回元組包含的元素個數。

print(min(a_tuple))
# min函數返回元組中最小的元素。

print(max(a_tuple))
# max函數返回元組中最大的元素。