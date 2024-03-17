"""
深拷贝会拷贝子对象， 而浅拷贝不会， 只拷贝父级对象
也就是说： 如果使用浅拷贝， 当你修改拷贝后的子对象的值（修改的前提是它可以修改， 如果他是不可变对象，修改相当于重新定义，地址会变），
那么原对象 同样会被修改， 因为他们实际是同一个子对象
"""

import copy

# 定义一个嵌套列表
original_list = [[1, 2, 3], [4, 5, 6], (1, 2)]

# 浅拷贝
shallow_copy = copy.copy(original_list)

# 深拷贝
deep_copy = copy.deepcopy(original_list)

# 修改原始列表的第一个子列表
original_list[0][0] = 100
# original_list[0] = [100, 200, 300]


# 打印结果
print("Original List:", original_list)
print("Original List id:", id(original_list))
print("Original List [0] 可变对象 id:", id(original_list[0]))
print("Original List [2] 不可变对象 id:", id(original_list[2]))
print()
print("Shallow Copy:", shallow_copy)
print("Shallow Copy id:", id(shallow_copy))
print("Shallow Copy [0] 可变对象 id:", id(shallow_copy[0]))
print("Shallow Copy [2] 不可变对象 id:", id(shallow_copy[2]))
print()
print("Deep Copy:", deep_copy)
print("Deep Copy id:", id(deep_copy))
print("Deep Copy [0] 可变对象 id:", id(deep_copy[0]))
print("Deep Copy [2] 不可变对象 id:", id(deep_copy[2]))

print(shallow_copy[2] is original_list[2])
"""
在这个示例中，我们修改了原始列表 original_list 的第一个子列表的第一个元素为 100。
由于浅拷贝 shallow_copy 只复制了对象本身，而不复制其子对象，所以当我们修改原始列表的子对象时，浅拷贝的结果也会受到影响。
因此，修改原始列表的子对象也会影响到浅拷贝的结果，这体现了浅拷贝只复制对象本身的特性。
"""
