"""
上下文管理器（Context Manager）是一种 Python 编程语言的功能，用于管理资源的分配和释放，确保资源在使用完毕后被正确释放，以避免资源泄漏。

在 Python 中，上下文管理器通常使用 with 语句来使用。一个实现了上下文管理器协议的对象可以被用作 with 语句的上下文，这意味着它可以定义 __enter__ 和 __exit__ 方法。

__enter__ 方法：进入上下文时执行的操作，在 with 语句块执行之前调用。
__exit__ 方法：退出上下文时执行的操作，在 with 语句块执行完毕后调用。
使用上下文管理器可以确保资源的正确分配和释放，即使在发生异常的情况下也能够正确地释放资源。

"""


class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")

    def do_something(self):
        print("Doing something")


# 使用上下文管理器
with MyContextManager() as cm:
    cm.do_something()


