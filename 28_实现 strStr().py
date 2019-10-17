class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack and needle:
            return -1
        elif not needle:
            return 0
        ls_hay = len(haystack)
        ls_needle = len(needle)
        for i in range(ls_hay-ls_needle + 1):
            if haystack[i:i+ls_needle] == needle:
                return i
        return -1