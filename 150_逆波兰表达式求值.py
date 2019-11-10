class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        d = {'+','-','*','/'}
        nums = []
        oprand = []
        for token in tokens:
            if token not in d:
                nums.append(token)
            else:
                num1 = str(nums.pop())
                num2 = str(nums.pop())
                res = int(eval(num2+token+num1))
                nums.append(res)
        return nums[0]