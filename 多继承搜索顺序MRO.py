"""
在 Python 2.x 中，存在着新式类（New-style classes）和旧式类（Old-style classes）的区别。
这个概念在 Python 3.x 中已经不存在了，因为在 Python 3.x 中，所有的类都是新式类。


经典类与新式类的区别是：继承搜索的顺序发生了改变，经典类多继承搜索顺序是深度优先， 按照从左至右的查找，并且将每一个父类的基类都查找一遍。
新式类则是， 先从左至右的查找， 然后再向每一个父类的基类进行查找。
（都是从左至右的顺序查找， 经典类查找一个父类时同时向上查找，新式类则是先查找所有的父类然后再向上查找）

MRO  方法解析顺序（Method Resolution Order，简称 MRO）
在 Python 中，当一个类继承自多个父类时，Python 使用一种称为 "C3 线性化（C3 Linearization）" 的算法来确定方法解析顺序

MRO 的计算遵循以下几个规则：
深度优先，从左向右： Python 使用深度优先搜索（Depth-First Search，DFS）的方式遍历类的继承关系树。在多重继承的情况下，Python 首先考虑最左边的父类，然后再考虑其他父类。
子类优先于父类： 在继承链中，子类的方法和属性会优先于父类的方法和属性。
继承顺序不变： 在计算 MRO 时，继承类的顺序不会改变。例如，如果类 A 继承自类 B 和类 C，那么在计算 MRO 时，类 B 的顺序会在类 C 的前面。
保持局部顺序： 如果类定义中指定了多个父类，Python 会保持这些父类之间的顺序。这意味着在 MRO 中，父类的顺序会保持与类定义时的顺序一致。
"""


class A:
    def __init__(self):
        print("Initializing class A")


class B(A):
    def __init__(self):
        print("Initializing class B")
        super().__init__()


class C(A):
    def __init__(self):
        print("Initializing class C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("Initializing class D")
        super().__init__()


# 创建对象实例
obj = D()


