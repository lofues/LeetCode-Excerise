class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ''
        strs.sort(key = len)
        _min = len(strs[0])
        prefix = ''
        for _ in range(_min):
            cur_str = strs[0][_]
            for string in strs:
                if string[_] != cur_str:
                    return prefix
            prefix += cur_str
        return prefix