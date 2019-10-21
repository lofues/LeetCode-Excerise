class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        def helper(idx,n,temp_list):
            res.append(temp_list)
            for i in range(idx,n):
                helper(i+1,temp_list + [nums[i]])
        helper(0,[])
        return res