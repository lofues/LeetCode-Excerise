class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            tmp = int(str(x)[::-1])
            return tmp if tmp <= 2 ** 31 - 1 else 0
        else:
            tmp = int(str(abs(x))[::-1])
            return -1 * tmp if tmp <= 2 ** 31 else 0
