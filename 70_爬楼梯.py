class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0: return 0
        elif n == 1: return 1
        elif n == 2: return 2
        queue = [1,2]
        for i in range(3,n+1):
            ret = queue.pop(0) + queue[0]
            queue.append(ret)
        return queue[-1]