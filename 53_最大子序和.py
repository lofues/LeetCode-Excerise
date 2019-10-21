class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 做筛选，如果最大值都小于0，则直接返回最大值
        max_num = max(nums)
        if max_num < 0:
            return max_num
        max_sum = min(nums)
        cur_sum = 0
        ans = (None,None)
        # 做累计加法，如果连续和小于0，则从下一个位置重新计数
        for j in range(len(nums)):
            cur_sum += nums[j]
            if cur_sum < 0:
                cur_sum = 0
            if cur_sum >= max_sum:
                max_sum = cur_sum
        return max_sum