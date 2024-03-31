

"""
pandas 的 数据类型
DataFrame 数据框
Series 数组
DataFrame 是 Series 的容器，Series 则是标量的容器
可以把 Series 理解为 DataFrame 的 一列， 多个 Series 组成 DataFrame

"""

import numpy as np
import pandas as pd

# df = pd.read_excel('trd_2014.xlsx')
#
# for col in df.columns:
#     print(col)
#     series = df[col]
#     print(type(series))

df2 = pd.DataFrame(np.random.randn(10, 4))
print(df2)

pieces = [df2[:2], df2[3:4], df2[-3:]]
for piece in pieces:
    print(piece)


# 结合 Concat
df_ = pd.concat(pieces)
"""
合并两个DataFrame
result = pd.concat([df1, df2], axis=0)  在行方向上连接
result = pd.concat([df1, df2], axis=1)  在列方向上连接

合并两个Series
result = pd.concat([s1, s2], axis=0)  在行方向上连接
"""

# 连接 merge

"""
就行 SQL 中的 Join
# 根据一个或多个键进行连接
result = pd.merge(df1, df2, on='key')  # 根据单个键连接
result = pd.merge(df1, df2, on=['key1', 'key2'])  # 根据多个键连接

# 指定连接方式
result = pd.merge(df1, df2, on='key', how='inner')  # 内连接
result = pd.merge(df1, df2, on='key', how='outer')  # 外连接
result = pd.merge(df1, df2, on='key', how='left')   # 左连接
result = pd.merge(df1, df2, on='key', how='right')  # 右连接
"""



"""
# 按照索引进行连接
result = df1.join(df2, how='inner')  # 内连接
result = df1.join(df2, how='outer')  # 外连接
result = df1.join(df2, how='left')   # 左连接
result = df1.join(df2, how='right')  # 右连接
"""

