class Solution:
    def findComplement(self, num: int) -> int:
        return 2**(len(bin(num).replace('0b',''))) - 1 - num