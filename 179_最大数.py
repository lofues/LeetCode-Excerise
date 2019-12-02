class LargestNumber(str):
    def __lt__(x,y):
        return x + y > y + x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums:return ''
        ret =  ''.join(sorted(map(str,nums),key=LargestNumber))
        return '0' if ret[0] == '0' else ret