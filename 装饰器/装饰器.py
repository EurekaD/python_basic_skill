"""
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

装饰器是 Python 中一种强大而灵活的功能，用于修改或扩展函数或类的行为。
它允许您在不修改原始代码的情况下包装或修改函数或方法。
装饰器通常用于添加新的功能、修改参数或结果，或者进行性能测量、日志记录等操作。
在 Python 中，装饰器是函数或类，它们接受一个函数作为输入并返回一个新的函数或修改后的类。
装饰器通过在要装饰的函数或类之前使用 @decorator_name 语法来应用。


functools.wraps 是 Python 中的一个装饰器，用于在定义装饰器时保留被装饰函数的元信息。
当你编写一个装饰器来包装另一个函数时，如果不使用 functools.wraps 装饰器，那么装饰器会导致被装饰函数的元信息（例如函数名称、文档字符串、参数列表等）丢失或被覆盖。

functools.wraps 装饰器的作用是将装饰器函数的元信息更新为被装饰函数的元信息，从而保留被装饰函数的原始信息。
这样做的好处是，通过 wraps 装饰器修饰后，被装饰函数将保留其原始名称、文档字符串和其他属性，这对于调试和代码理解非常有帮助。

常见装饰器
@property 修饰方法，使方法作为属性使用
@abstractmethod 抽象方法表示基类的一个方法，没有实现，所以基类不能实例化，子类实现了该抽象方法才能被实例化。
@classmethod 不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。其实，静态方法就是普通的函数，只是碰巧在类的定义体中，而不是在模块层定义
@staticmethoed 也不需要self参数，但第一个参数需要是表示自身类的cls参数。


实际应用时发现的小问题：
1.注意参数的传递
被装饰的函数如果有参数，装饰器需要正确地处理这些参数。
装饰器的作用是包装被装饰函数，因此装饰器函数中的 wrapper 函数需要接受与被装饰函数相同的参数，并将这些参数传递给被装饰函数。
因此，在编写装饰器时，需要确保装饰器中的 wrapper 函数能够接受任意数量的位置参数和关键字参数，并将它们正确传递给被装饰的函数。
通常情况下，使用 *args 和 **kwargs 来实现这一点，这样可以接受任意数量和类型的参数。
2.装饰器可以连续使用多个，注意使用的顺序
3.如果被装饰函数有返回值，要在装饰器的函数里自己处理
4.递归函数装饰会出现问题
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


@my_decorator1
def say_hello1():
    """say_hello1()"""
    print("say_hello1():Hello!")


@my_decorator2
def say_hello2():
    """say_hello2()"""
    print("say_hello2():Hello!")


say_hello1()
# 输出函数的元信息
# print("Function name:", say_hello1.__name__)
# print("Function docstring:", say_hello1.__doc__)

# print("Function name:", say_hello2.__name__)
# print("Function docstring:", say_hello2.__doc__)



