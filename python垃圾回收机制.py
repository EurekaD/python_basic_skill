"""
名称类型的确定、内存空间的分配与释放都是由python解释器在运行时进行的。
python这一自动管理内存功能极大的减小了程序员负担,这也是成就python自身的重要原因之一。

引用计数为主， 标记清除、分代回收为辅

引用计数：
简单，高效，具有实时性  但是 不能处理循环引用

标记-清除：
标记-清除算法（Mark and Sweep Algorithm）是一种常见的垃圾回收算法，用于检测和释放不再被程序使用的内存。以下是标记-清除算法的详细步骤：

1. 标记阶段（Mark Phase）：
a. 初始标记（Initial Marking）：
从根对象（如全局变量、栈、寄存器等）开始，标记所有直接可达的对象。这是一个快速的阶段，只标记直接可达的对象，不处理对象间的引用关系。
b. 追踪标记（Trace Marking）：
遍历被标记的对象，逐步追踪并标记它们引用的对象。这一步骤通过深度优先搜索或广度优先搜索等方式完成。
c. 并发标记（Concurrent Marking）：
一些现代的垃圾回收器尝试在程序执行的同时进行标记，以减少暂停时间。这就是并发标记。

2. 清除阶段（Sweep Phase）：
a. 清除不可达对象（Sweep Unmarked）：
遍历整个堆内存，清除所有未被标记的对象。这些未被标记的对象被认为是不再被程序引用的垃圾。
b. 更新引用关系：
在清除阶段完成后，需要更新所有指向已被清除对象的引用，将它们置为NULL或其他合适的值。


分代回收
分代回收是基于这样的一个统计事实，对于程序，存在一定比例的内存块的生存周期比较短；
而剩下的内存块，生存周期会比较长，甚至会从程序开始一直持续到程序结束。
生存期较短对象的比例通常在 80%～90% 之间，这种思想简单点说就是：对象存在时间越长，越可能不是垃圾，应该越少去收集。
这样在执行 标记-清除 算法时可以有效减小遍历的对象数，从而提高垃圾回收的速度。
Python将所有对象分成了三代， 对象存活时间越长就越晚被回收， 反之则越早被回收。

"""
import sys
import gc

# 引用计数+清理
a = 1
print(sys.getrefcount(a))


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


# 创建两个节点，并形成循环引用
node1 = Node(1)
node2 = Node(2)
node1.next_node = node2
node2.next_node = node1


# 手动删除引用，使得垃圾回收无法解决循环引用的问题
node1 = None
node2 = None

# print(sys.getrefcount(node1))
# print(sys.getrefcount(node2))

print(gc.garbage)
# 尝试手动触发垃圾回收
gc.collect()

# 检查循环引用是否导致内存无法释放
print(gc.garbage)
