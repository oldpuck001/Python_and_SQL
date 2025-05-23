# str_basic.py

a_str = 'Hello'

# 字符串的索引：第一個元素的索引是0；最後一個元素的索引是 -1
print('字符串的索引')
print(a_str[-1])

# 字符串的切片：第一個索引是包含的第一個元素的編號，第二個索引是切片後餘下的第一個元素的編號。
print('字符串的切片')
print(a_str[1:3])

# 字符串的相加（拼接字符串）：+，用加法運算符相加，不能拼接不同類型的序列。
print('字符串的相加（拼接字符串）')
print(a_str + ' world!')

# 字符串的乘法：*，將序列與數x相乘時，將重複這個序列x次來創建一個新序列。
print('字符串的乘法')
print(a_str * 3)

# 字符串的成員資格檢查：in，要檢查特定的值是否包含在序列中，可以使用運算符in，包含返回True，不包含返回False。
print('字符串的成員資格檢查')
if 'e' in a_str:
    print('e is in hello.')