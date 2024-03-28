
"""
基础不牢， 地动山摇

"""

import pandas as pd


# 时间特征 的 操作

# 读取的时候指定为日期时间类型
raw = pd.read_excel("trd_2014.xlsx", parse_dates=['Trddt'])

# 取最新时间
latest_date = raw['Trddt'].max()

# 取十一月的数据
raw_mo11 = raw[raw['Trddt'].dt.month == 11]


# 取一定时间范围的数据
start_date = '2014-01-01'
end_date = '2014-01-31'
# Pandas 库能够处理字符串和日期时间类型之间的比较运算
selected_data = raw[(raw['Trddt'] >= start_date) & (raw['Trddt'] <= end_date)]







