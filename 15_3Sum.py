class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        k = 0
        ret = []
        while k < len(nums) and nums[k] <= 0:
            while 0 < k < len(nums) and nums[k] == nums[k-1]:
                k += 1
            i, j = k + 1, len(nums) - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == 0: 
                    ret.append([nums[k],nums[i],nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                elif s < 0: 
                    i += 1
                    while i < j and nums[i] == nums[i-1]: i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j+1]: j -= 1
            k += 1
        return ret