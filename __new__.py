

class A(object):
    def __init__(self):
        print("__init__")

    def __new__(cls, *args, **kwargs):
        print("这是 cls 的 ID", id(cls))
        print("这是 new 的方法", object.__new__(cls))
        return object.__new__(cls)


A()
# cls 就是 创建的实例类 A()
print("这是类A的ID", id(A))


