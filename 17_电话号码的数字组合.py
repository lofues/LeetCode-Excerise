class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':return []
        _dict = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        result = []
        for digit in digits:
            if not result:
                result += [i for i in _dict[digit]]
            else:
                result = [k + v for k in result for v in _dict[digit]]
        return result