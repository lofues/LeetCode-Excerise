class Solution:
    def isHappy(self, n: int) -> bool:
        # 使用集合记录结果
        # 如果重复出现在集合中的元素且没有出现过1，就返回False
        if n <= 0:return False
        def handle(num):
            ret = 0
            while num != 0:
                temp = num % 10
                ret += temp ** 2
                num //= 10
            return ret
        mem = set()
        ret = handle(n)
        while ret != 1 and ret not in mem:
            mem.add(ret)
            ret = handle(ret)
        return ret == 1