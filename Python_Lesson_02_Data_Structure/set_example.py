# set_example.py

a_set = {0,1,2,3,0,1,2,3,4,5}
b_set = set(range(10))
c_set = set()
d_set = {None,}

print(a_set)
print(b_set)
print(c_set)
print(type(c_set))
print(d_set)
print(type(d_set))

# 集合的運算符：
# 並集
e_set = a_set | b_set
print(e_set)

# 交集
f_set = a_set & b_set                        
print(f_set)

# a和b的對稱差集
g_set = a_set ^ b_set
print(g_set)

h_set = a_set - b_set
print(h_set)

i_set = b_set - a_set
print(i_set)

# <=
print(a_set <= b_set)

# >=
print(b_set >= a_set)

# 集合方法
# 並集
j_set = a_set.union(b_set)
print(j_set)

# 交集
k_set = a_set.intersection(b_set)
print(k_set)

# add方法
j_set.add(100)
print(j_set)
# 將1個方法添加到集合中

# remove方法
j_set.remove(100)
print(j_set)
# 從集合中移除指定元素，如果元素不存在，則引發KeyError異常

# difference方法
l_set = b_set.difference(a_set)
print(l_set)
# 返回集合a中有而集合b中没有的元素组成的新集合

# symmetric_difference方法
m_set = a_set.symmetric_difference(b_set)
print(m_set)
# 返回一個新的集合，其中包含所有在集合a或集合b中出現，但不同時出現在兩個集合中的元素。可以理解為取兩個集合的對稱差集。

# issubset方法
print(a_set.issubset(b_set))
# 接受一個集合作為參數，並返回一個布爾值表示當前集合是否是該參數集合的子集，子集的相對概念是超集。

# copy方法
n_set = a_set.copy()
print(n_set)
# 用於返回一個集合（set）的複製。這個方法將返回一個包含原始集合中所有元素的新集合，對這個新集合的任何更改都不會影響原始集合。

# 使用集合對列表或者元组去重
o_set = set(["USD", "USD", "SGD", "EUR", "USD", "EUR"])
p_set = set(("USD", "USD", "SGD", "EUR", "USD", "EUR"))
print(o_set)
print(p_set)