import threading
import queue

class ZeroEvenOdd(object):
    def __init__(self, n):
        self.n = n
        self.z = threading.Semaphore(1)
        self.o = threading.Semaphore(0)
        self.e = threading.Semaphore(0)

    def zero(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1):
            self.z.acquire()
            printNumber(0)
            if i % 2 == 1:
                self.o.release()
            else:
                self.e.release()

    def even(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(2, self.n + 1, 2):
            self.e.acquire()
            printNumber(i)
            self.z.release()

    def odd(self, printNumber):
        """
        :type printNumber: method
        :rtype: void
        """
        for i in range(1, self.n + 1, 2):
            self.o.acquire()
            printNumber(i)
            self.z.release()
