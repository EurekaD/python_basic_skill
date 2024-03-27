

import pandas as pd
# import chardet

# with open('trd_2014.xlsx', 'rb') as f:
#     result = chardet.detect(f.read())
#
# print(result['encoding'])

raw = pd.read_csv("trd_2014.xlsx")

print(raw.head())

