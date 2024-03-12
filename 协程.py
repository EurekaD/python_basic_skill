"""
协程: 协程，又称微线程，纤程，英文名Coroutine。协程的作用，是在执行函数A时，可以随时中断，去执行函数B，然后中断继续执行函数A（可以自由切换）。
但这一过程并不是函数调用（没有调用语句），这一整个过程看似像多线程，然而协程只有一个线程执行.
在Python3.4之前，官方没有对协程的支持，存在一些三方库的实现，比如gevent和Tornado。3.4之后就内置了asyncio标准库，官方真正实现了协程这一特性。
而Python对协程的支持，是通过Generator实现的，协程是遵循某些规则的生成器。因此，我们在了解协程之前，我们先要学习生成器。

"""

# __next__()方法: 作用是启动或者恢复generator的执行，相当于send(None)
# send(value)方法：作用是发送值给yield表达式。启动generator则是调用send(None)


def consumer():
    print("[CONSUMER] start")
    r = 'start'
    while True:
        n = yield r
        if not n:
            print("n is empty")
            continue
        print("[CONSUMER] Consumer is consuming %s" % n)
        r = "200 ok"


def producer(c):
    # 启动generator
    start_value = c.send(None)
    print(start_value)
    n = 0
    while n < 3:
        n += 1
        print("[PRODUCER] Producer is producing %d" % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    # 关闭generator
    c.close()

# # 创建生成器
# c = consumer()
# # 传入generator
# producer(c)
# 子生成器

#  yield from
# Python3.3版本新增yield from语法
# 新语法用于将一个生成器部分操作委托给另一个生成器。
# 此外，允许子生成器（即yield from后的“参数”）返回一个值，该值可供委派生成器（即包含yield from的生成器）使用。
# 并且在委派生成器中，可对子生成器进行优化。
# 可以用来处理异常， 放在委派生成器中 yield from 的前后


def test(n):
    i = 0
    while i < n:
        yield i
        i += 1


# 委派生成器
def test_yield_from(n):
    print("test_yield_from start")
    yield from test(n)
    print("test_yield_from end")


# for i in test_yield_from(3):
#     print(i)


# 协程
# Python3.4开始，新增了asyncio相关的API，语法使用`@asyncio.coroutine和yield from`实现协程
# Python3.5中引入async/await语法
# async/await实际上只是`@asyncio.coroutine和yield from`的语法糖：
# 把 @asyncio.coroutine 替换为 async
# 把 yield from         替换为 await
import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


loop = asyncio.get_event_loop()
print("start")
loop.run_until_complete(print_sum(1, 2))
print("end")
loop.close()

