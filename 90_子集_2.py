class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        nums.sort()
        def helper_1(idx,n,temp_list):
            if temp_list not in res:
                res.append(temp_list)
            for i in range(idx,n):
                helper(i+1,n,temp_list+[nums[i]])
        def helper_2(idx,n,temp_list):
            res.append(temp_list)
            for i in range(idx,n):
                # 当遇见重复元素时，只执行第一次
                if i > idx and nums[i] == nums[i-1]:
                    continue
                helper_2(i+1,n,temp_list+[nums[i]])
        # helper_1(0,n,[])
        helper_2(0,n,[])
        return res