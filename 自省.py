"""
自省是指一个对象能够访问自身的属性和方法，并能够了解自身的类型。在 Python 中，自省是一种非常强大和灵活的特性，它使得程序能够在运行时检查对象的属性和方法，从而动态地进行操作。

Python 中的一些内置函数和特殊方法可以用于实现自省：

type(obj): 返回对象的类型。

dir(obj): 返回对象的属性和方法列表。

hasattr(obj, attr): 判断对象是否有指定的属性。

getattr(obj, attr): 获取对象的指定属性。

setattr(obj, attr, value): 设置对象的指定属性。

delattr(obj, attr): 删除对象的指定属性。

isinstance(obj, class): 判断对象是否是指定类的实例。

issubclass(subclass, class): 判断一个类是否是另一个类的子类。

"""

student = {
    "name": "chenlin",
    "age": 22
}

print(dir(student))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__',
# '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy',
# 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

print(dir(object))
# ['__class__', '__delattr__',
# '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
# '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__']

