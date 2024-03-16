"""
类似于 全局变量 ，
我的应用示例是 用在模型部署，
LLM 很大，每次加载都很慢，所以使用单例模式（用装饰器实现的）来获取模型实例

"""


def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]

    return inner


@singleton
class Cls(object):
    def __init__(self):
        pass


cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


