class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s: str) -> bool:
            stack = []
            for i in s:
                if i == '(' or not stack:
                    stack.append(i)
                elif i == ')' and stack[-1] == ')':
                    return False
                elif i == ')':
                    stack.pop()
                else:
                    return False
            return True if not stack else False
        undumplicate = []
        temp = ['(',')']
        for i in range(n * 2):
            if not undumplicate:
                undumplicate += [i for i in temp]
            else:
                undumplicate = [r + v for r in undumplicate for v in temp]
        _del = []
        for i in undumplicate:
            if isValid(i) == False:
                _del += [i]
        for s in _del:
            undumplicate.remove(s)
        return undumplicate