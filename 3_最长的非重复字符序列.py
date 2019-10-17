class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return  0
        if len(s) == 1: return 1
        left = 0
        max_length = 0
        ret = set()
        for char in s:
            if char in ret:
                while s[left] != char:
                    ret.remove(s[left])
                    left += 1
                ret.remove(char)
                left += 1
            ret.add(char)
            max_length = len(ret) if len(ret) > max_length else max_length
        return max_length