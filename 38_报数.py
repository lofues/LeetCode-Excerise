class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        tmp = '1'
        for i in range(n - 1):
            tmp = self.count(tmp)
        return tmp

    def count(self, x):
        result = []
        i = j = 0
        _list = list(x)
        _list.append(None)
        while j < len(_list) - 1:
            j += 1
            if _list[i] != _list[j]:
                result.extend([j - i, _list[i]])
                i = j
        return ''.join([str(s) for s in result])
