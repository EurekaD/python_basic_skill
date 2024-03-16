"""
Least Recently Used，最近最少使用
该模块包含在标准库中，非常易于使用。它还包含比这个装饰器更酷的功能，但这个装饰器肯定是我最喜欢的。
此装饰器可用于使用缓存加速函数的连续运行。当然，这应该在使用时记住一些关于缓存的注意事项，但在通用使用情况下，大多数时候这个装饰器是值得使用的。
能够用一个简单的装饰器来加速代码是非常棒的。
可以从这样的装饰器中受益的函数的一个很好的例子是递归函数，例如计算阶乘的函数：

"""

from functools import lru_cache, wraps
import time


@lru_cache
def factorial1(n):
    return n * factorial1(n-1) if n else 1


# 递归在计算时间上可能非常困难，但添加此装饰器有助于显着加快此函数的连续运行速度。
# 现在每当我们运行这个函数时，前几个阶乘计算将被保存到缓存中。
# 因此，下次我们调用该函数时，我们只需要计算我们之前使用的阶乘之后的阶乘。
# 当然，并不是所有的阶乘计算都会被保存，但是很容易理解为什么这个装饰器的一个很好的应用程序来加速一些自然很慢的代码。

@lru_cache
def factorial2(n):
    return n * factorial2(n-1) if n else 1


# print(factorial1(1000))
if __name__ == "__main__":
    print(factorial2(100))
    # print(factorial1.__name__)





