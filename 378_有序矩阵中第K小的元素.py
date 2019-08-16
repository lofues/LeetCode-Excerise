class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        nums = []
        for _ in matrix:
            nums.extend(_)
        nums.sort()
        if k > len(nums):
            return None
        else:
            return nums[k-1]