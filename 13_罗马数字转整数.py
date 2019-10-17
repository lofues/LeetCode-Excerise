class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:return 0
        result = 0
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        if len(s) == 1:return d[s]
        for i,c in enumerate(s):
            if i == len(s) - 1:
                result += d[c]
            else:
                if d[c] < d[s[i+1]]:
                    result -= d[c]
                else:
                    result += d[c]
        return result