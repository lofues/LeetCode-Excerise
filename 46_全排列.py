class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        def helper(nums,temp_list):
            if not nums:
                ret.append(temp_list)
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:],temp_list+[nums[i]])
        helper(nums,[])
        return ret