import threading
# 方法一 使用互斥锁
class Foo:
    def __init__(self):
        self.lock1 = threading.Lock()
        self.lock2 = threading.Lock()
        self.lock1.acquire()
        self.lock2.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.lock1.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.lock1.acquire()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.lock1.release()
        self.lock2.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        self.lock2.acquire()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()
        self.lock2.release()

# 方法2 使用condition 同步信号量
# If the calling thread has not acquired the lock when this method is
#         called, a RuntimeError is raised.
#
#         This method releases the underlying lock, and then blocks until it is
#         awakened by a notify() or notify_all() call for the same condition
#         variable in another thread, or until the optional timeout occurs. Once
#         awakened or timed out, it re-acquires the lock and returns.
import threading
class Foo:
    def __init__(self):
        self.c = threading.Condition()
        self.t = 0

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        with self.c:
            # wait_for 传入一个 callable 对象返回True时执行，False 时释放锁
            self.c.wait_for(lambda:self.t == 0)
            printFirst()
            self.t += 1
            self.c.notify_all()



    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self.c:
            self.c.wait_for(lambda:self.t == 1)
            printSecond()
            self.t += 1
            self.c.notify_all()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self.c:
            self.c.wait_for(lambda:self.t == 2)
            printThird()
            self.t += 1
            self.c.notify_all()