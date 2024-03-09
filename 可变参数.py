"""
*args, **kwargs是什么意思?

可变参数 指 允许函数接受多个不确定参数的用法， 分为两种类型 【args 和 kwargs 只是约定】
优点： 有利于编写 通用函数或库
1. *      arguments
可变位置参数，把传入的多个参数变为元组

2 **   Keyword arguments
可变关键字参数，把传入的多个参数变为字典

在Python3.5以上版本
*和**多了一个功能叫做解包(unpacking)。

"""


def fun(*args):
    print(args)


def fun1(**kwargs):
    print(kwargs)


if __name__ == "__main__":
    fun(1, 2, 3, 4, 5)

    # fun1(1, 2, 3, 4, 5)  TypeError: fun1() takes 0 positional arguments but 5 were given

    fun1(a=1, b=2, c=3)



