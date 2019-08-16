class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return
        b = [0] * 3
        for i in range(len(nums)):
            # 统计各个元素个数
            b[nums[i]] += 1
        for i in range(1,len(b)):
            # 将各个位置统计为小于这个元素的个数
            b[i] += b[i-1]
        c = [0] * len(nums)
        for i,val in enumerate(nums[::-1]):
            index = b[val] - 1
            c[index] = val
            b[val] -= 1
        nums[::] = c[::]