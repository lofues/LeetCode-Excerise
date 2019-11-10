class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums: return
        if len(nums) == 1: return nums[0]
        # 使用动态规划
        # 记录i位置之前的最大值和最小值
        pre_max = nums[0]
        pre_min = nums[0]
        res = nums[0]
        for num in nums[1:]:
            cur_max = max(num,pre_max*num,pre_min*num)
            cur_min = min(num,pre_max*num,pre_min*num)
            res = max(cur_max,res)
            pre_max = cur_max
            pre_min = cur_min
        return res