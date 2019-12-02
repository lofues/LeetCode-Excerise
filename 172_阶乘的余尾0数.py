class Solution:
    # 5-> 一个0   25-> 两个0  125-> 三个0 以此类推
    def trailingZeroes(self, n: int) -> int:
        if n<=4:return 0
        ret = 0
        while n > 0:
            ret += n // 5
            n //= 5
        return ret

