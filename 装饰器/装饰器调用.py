from functools import wraps

"""
发现一个问题：
如果在装饰器要返回的函数之外写一些语句，在使用给被装饰函数使用装饰器时就会调用这部分代码
虽然后来想起来显而易见，但还是记录一下
"""


def my_decorator2(func):
    @wraps(func)
    def wrapper():
        print("my_decorator2：Something is happening before the function is called.")
        func()
        print("my_decorator2：Something is happening after the function is called.")
    print("my_decorator2：该装饰器被使用")
    return wrapper


@my_decorator2
def say_hello2():
    """say_hello2()"""
    print("say_hello2():Hello!")