import copy

# 定义一个嵌套列表
original_list = [[1, 2, 3], [4, 5, 6]]

# 浅拷贝
shallow_copy = copy.copy(original_list)

# 深拷贝
deep_copy = copy.deepcopy(original_list)

# 修改原始列表的第一个子列表
original_list[0][0] = 100

# 打印结果
print("Original List:", original_list)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)

"""
在这个示例中，我们修改了原始列表 original_list 的第一个子列表的第一个元素为 100。
由于浅拷贝 shallow_copy 只复制了对象本身，而不复制其子对象，所以当我们修改原始列表的子对象时，浅拷贝的结果也会受到影响。
因此，修改原始列表的子对象也会影响到浅拷贝的结果，这体现了浅拷贝只复制对象本身的特性。
"""
