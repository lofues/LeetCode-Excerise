class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        floor = 1
        while s:
            cur = s[-1]
            res += (ord(cur) - 64) * floor
            floor *= 26
            s = s[:-1]
        return res