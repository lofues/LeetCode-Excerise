class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        # 小于等于都应加入栈顶，因为可以有重复值
        if not self.min or x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        if self.stack.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return self.min[-1] if self.min else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()