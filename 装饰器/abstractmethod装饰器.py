"""
abc.ABC 是 Python 中 abc（Abstract Base Classes）模块中的一个类，用于定义抽象基类（Abstract Base Class）。
抽象基类提供了一种方式来定义接口和规范子类必须实现的方法和属性。
abc.ABC 类本身并不做太多的事情，它只是一个基类，用于表示其他类是抽象基类。通常情况下，你不会直接继承 abc.ABC 类，而是通过继承它的子类来创建自己的抽象基类。

ABCMeta 是 Python 中 abc 模块中的一个元类，用于定义抽象基类（Abstract Base Class）的行为。
元类是 Python 中的一种特殊的类，它用于创建其他类。在 abc 模块中，ABCMeta 元类被用来创建抽象基类，它的主要作用是确保抽象基类的行为和特性。
"""

from abc import ABC, ABCMeta, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 必须实现这两个抽象方法，否则报错
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# 创建对象实例
rect = Rectangle(5, 4)

# 输出矩形的面积和周长
print("Area:", rect.area())
print("Perimeter:", rect.perimeter())