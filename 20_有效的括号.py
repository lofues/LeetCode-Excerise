class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        _dict = {
            '(':')',
            '[':']',
            '{':'}'
        }
        stack = []
        for i in s:
            if i in _dict.keys() or not stack:
                stack.append(i)
            elif i in _dict.values() and stack[-1] in _dict.values():
                return False
            elif i == _dict[stack[-1]]:
                stack.pop()
            else:
                return False
        return True if not stack else False