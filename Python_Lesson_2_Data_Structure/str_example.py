# str_example.py

a_str = 'Hello'
b_str = '$$$ Get rich now!!! $$$'
c_str = 'abcdefghijk'
e_str = '    abcd  '
f_str = '*** ABCDefghijk!!! **'
j_str = '1+2+3+4+5'
k_str = '/usr/bin/env'
l_str = 'Using the default'

# 字符串操作：
# 字符串的索引
print(a_str[-1])
# 第一個元素的索引是0；最後一個元素的索引是 -1

# 字符串的切片
print(a_str[1:3])
# 第一個索引是包含的第一個元素的編號，第二個索引是切片後餘下的第一個元素的編號。

# 字符串的相加（拼接字符串）：+
print(a_str + ' world!')
# 用加法運算符相加，不能拼接不同類型的序列。

# 字符串的乘法：*
print(a_str * 3)
# 將序列與數x相乘時，將重複這個序列x次來創建一個新序列。

# 成員資格檢查：in
if 'e' in a_str:
    print('e is in hello.')
# 要檢查特定的值是否包含在序列中，可以使用運算符in，包含返回True，不包含返回False。

# 字符串函數：
print(len(a_str))
# len函數返回序列包含的元素個數。

print(min(a_str))
# min函數返回序列中最小的元素。

print(max(a_str))
# max函數返回序列中最大的元素。

# 字符串方法：
print(b_str)
print(b_str.find('$$$'))
print(b_str.find('$$$', 1))         # 只指定了起点
print(b_str.find('!!!'))
print(b_str.find('!!!', 0, 16))     # 同时指定了起点和终点
# find方法在字符串中查找子串，可以用in方法檢查也可使用find來執行。如果找到，就返回子串的第一個字符的索引，否則返回-1。
# 還可指定搜索的起點和終點（它們都是可選的）。請注意，起點和終點值（第二個和第三個參數）指定的搜索範圍包含起點，但不包含終點。

d_str = c_str.replace('bc', 'xyz')
print(d_str)
# replace方法將指定子串替換為另一個並返回，並返回替換後的結果。因為字符串是不可變的，所以所有的元素賦值和切片賦值都是非法的。

g_str = e_str.strip('')
print(g_str)
h_str = f_str.strip(' *!')
print(h_str)
# strip方法將字符串開頭和末尾的指定字符串刪除，並返回刪除後的結果，默認情況下刪除的是開頭和末尾的空白。
# 這個方法只刪除開頭或末尾的指定字符，因此中間的指定字符不會被刪除。

i_str = a_str.lower()
print(i_str)
# lower方法返回字符串的小寫版本。

m_str = j_str.split('+')
print(m_str)
n_str = k_str.split('/')
print(n_str)
o_str = l_str.split()
print(o_str)
# split方法用於將字符串拆分為序列。注意，如果没有指定分隔符，将默认在单个或多个连续的空白字符（空格、制表符、换行符等）处进行拆分。

seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))
dirs = ('', 'usr', 'bin', 'env')
print('/'.join(dirs))
# join方法通過使用不同的分隔符，將序列的元素合併為一個字符串。所有合併序列的元素必須都是字符串。