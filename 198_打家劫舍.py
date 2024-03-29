class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:return 0
        if len(nums) == 1:return nums[0]
        dp = [0 for i in range(len(nums))]
        dp[0],dp[1] = nums[0],max(nums[1],nums[0])
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return max(dp[-1],dp[-2])