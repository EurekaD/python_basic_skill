import pandas as pd

"""
read_csv 函数：
用于读取逗号分隔值（CSV）文件。
默认使用逗号作为字段分隔符。
默认使用 UTF-8 编码打开文件。
可以通过参数指定其他分隔符、编码、行、列等参数。

read_table 函数：
用于读取通用的文本文件。
可以指定任意的字段分隔符，默认分隔符为制表符（\t）。
默认使用 UTF-8 编码打开文件。
可以通过参数指定其他分隔符、编码、行、列等参数。

因此，read_csv 和 read_table 在功能上是类似的，都可以用于读取文本文件，但 read_csv 更适合读取逗号分隔的文件，而 read_table 则更灵活，
可以读取任意分隔符的文件。通常情况下，你可以根据文件的特点选择使用其中一个函数。

如果是 Microsoft Excel 文件  .xlsx格式的表格 需要使用 read_excel
[需要安装 openpyxl]
"""

# 尝试使用默认编码打开文件
# read_csv 函数的默认编码通常是 UTF-8
# df = pd.read_csv("trd_2014.xlsx")


# 尝试使用不同的编码打开文件
encodings = ['utf-8', 'gbk', 'iso-8859-1']
for encoding in encodings:
    try:
        df = pd.read_excel('trd_2014.xlsx', encoding=encoding)
        print("成功使用编码 {} 打开文件。".format(encoding))
        break
    except Exception as e:
        print("使用编码 {} 打开文件时出现错误：{}".format(encoding, e))


# 输出文件的 编码类型
# import chardet

# with open('trd_2014.xlsx', 'rb') as f:
#     result = chardet.detect(f.read())
#
# print(result['encoding'])
