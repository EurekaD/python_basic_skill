"""
这些数据类型不可变：
数字
字符串
元组
布尔值
不可变集合
冻结字典


可变：
列表， 字典，集合
"""

# 这算是重定义
x = 3
x = 4.1


str_0 = "hello"


for i in str_0:
    print(i)
# str_0[0] = '1'
print(str_0[0])

# 不可变集合
my_frozenset = frozenset([1, 2, 3])