
# 受到 GIL 的影响， 限制多线程并行执行 CPU 密集型任务。主要用于 I/O 密集型任务。

from threading import Thread

"""
关于线程信息的函数：

threading.active_count()：返回当前存活的Thread对象数量。
threading.current_thread()：返回当前线程的Thread对象。
threading.enumerate()：列表形式返回所有存活的Thread对象。
threading.main_thread()：返回主Thread对象。


Thread对象的方法及属性：

Thread.name：线程的名字，没有语义，可以相同名称。
Thread.ident：线程标识符，非零整数。
Thread.+：是否为守护线程。
Thread.is_alive()：是否存活。
Thread.start()：开始线程活动。若多次调用抛出RuntimeError。
Thread.run()：用来重载的，
Thread.join(timeout=None)：等待直到线程正常或异常结束。尚未开始抛出RuntimeError
Thread(group=None, target=None, name=None, args=(), kwargs={}, *, deamon=None)：构造函数。

如果某个线程是守护线程，那么这个线程会在主线程运行完毕后结束。
主线程运行完毕指的是主线程的进程内所有非守护线程全部运行完毕，所以可以理解为守护进程是不那么重要的进程。
"""

import time
from threading import Thread


def task1():
    print("开始做任务1啦")
    time.sleep(1)  # 用time.sleep模拟任务耗时
    print("任务1结束啦")


def task2():
    print("开始做任务2啦")
    for i in range(5):
        print("任务2-{}".format(i))
        time.sleep(1)
    print("任务2结束啦")


if __name__ == '__main__':
    print("这里是主线程")
    # 创建线程对象
    t1 = Thread(target=task1)
    t2 = Thread(target=task2)
    t2.setDaemon(True)  # 设置为守护进程，必须在start之前
    # 启动
    t1.start()
    t2.start()
    time.sleep(0.3)
    print("主线程结束了")
