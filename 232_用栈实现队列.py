class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.stack_pop:
            self.stack_push.append(self.stack_pop.pop())
        self.stack_push.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        else:
            while self.stack_push:
                self.stack_pop.append(self.stack_push.pop())
            return self.stack_pop.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        elif not self.stack_pop:
            return self.stack_push[0]
        else:
            return self.stack_pop[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.stack_push or self.stack_pop)

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()