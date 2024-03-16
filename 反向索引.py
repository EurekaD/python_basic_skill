"""
在Python中，可以使用字典（Dictionary）实现反向索引。
反向索引是指根据值查找对应的键，而不是根据键查找对应的值

"""

# 原始索引
index = {
    "apple": [0, 3, 6],
    "banana": [1, 4],
    "orange": [2, 5]
}

# 反向索引
reverse_index = {}

# 构建反向索引
for key, values in index.items():
    for value in values:
        if value in reverse_index:
            reverse_index[value].append(key)
        else:
            reverse_index[value] = [key]

# 输出反向索引
for key, values in reverse_index.items():
    print(f"{key}: {values}")
