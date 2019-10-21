class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def helper(nums,temp_list):
            if not nums:
                res.append(temp_list)
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                helper(nums[:i]+nums[i+1:],temp_list+[nums[i]])
        helper(nums,[])
        return res