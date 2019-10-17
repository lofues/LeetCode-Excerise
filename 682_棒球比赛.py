class Solution:
    def calPoints(self, ops: List[str]) -> int:
        num_stack = []
        while ops:
            x = ops.pop(0)
            if x == 'C':
                if num_stack:
                    num_stack.pop()
            elif x == 'D':
                if num_stack:
                    num_stack.append(num_stack[-1] * 2)
            elif x == '+':
                if len(num_stack) >= 2:
                    num_stack.append(num_stack[-1] + num_stack[-2])
                elif len(num_stack) == 1:
                    num_stack.append(num_stack[-1])
            else:
                num_stack.append(int(x))
        return sum(num_stack) if num_stack else None