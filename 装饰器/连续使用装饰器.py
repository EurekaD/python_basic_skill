"""


"""

from functools import wraps

def my_decorator1(func):
    def wrapper():
        print("my_decorator1：Something is happening before the function is called.")
        func()
        print("my_decorator1：Something is happening after the function is called.")
    print("my_decorator1：该装饰器被使用")
    return wrapper


def my_decorator2(func):
    @wraps(func)
    def wrapper():
        print("my_decorator2：Something is happening before the function is called.")
        func()
        print("my_decorator2：Something is happening after the function is called.")
    print("my_decorator2：该装饰器被使用")
    return wrapper


@my_decorator2
@my_decorator1
def say_hello1():
    """say_hello1()"""
    print("say_hello1():Hello!")


say_hello1()
