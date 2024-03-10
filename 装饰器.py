"""
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

装饰器是 Python 中一种强大而灵活的功能，用于修改或扩展函数或类的行为。
它允许您在不修改原始代码的情况下包装或修改函数或方法。
装饰器通常用于添加新的功能、修改参数或结果，或者进行性能测量、日志记录等操作。
在 Python 中，装饰器是函数或类，它们接受一个函数作为输入并返回一个新的函数或修改后的类。
装饰器通过在要装饰的函数或类之前使用 @decorator_name 语法来应用。

"""


def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    print("Test")
    return wrapper


@my_decorator
def say_hello():
    print("Hello!")

say_hello()

