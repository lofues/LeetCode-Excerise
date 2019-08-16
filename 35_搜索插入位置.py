class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        ls = len(nums)
        if ls == 0:
            return 0
        for i in range(ls):
            if not i:
                if target <= nums[i]:
                    return i
                else:
                    continue
            elif nums[i - 1] < target <= nums[i]:
                return i
        return ls
