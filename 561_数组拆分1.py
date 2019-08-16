class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        new_nums = sorted(nums)
        return sum((new_nums[i] for i in range(0, len(nums), 2)))
