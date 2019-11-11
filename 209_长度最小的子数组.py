class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:return 0
        if nums[0] >= s: return 1
        min_len = float('inf')
        i,j = 0,1
        while j < len(nums):
            if i == j:
                if nums[i] >= s:
                    return 1
                else:
                    j += 1
                    continue
            if sum(nums[i:j+1]) >= s:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                i += 1
            else:
                j += 1
        return 0 if min_len > len(nums) else min_len