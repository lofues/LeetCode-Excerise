class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        i, j = 0, len(nums) - k - 1
        m, n = len(nums) - k, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        while m < n:
            nums[m], nums[n] = nums[n], nums[m]
            m += 1
            n -= 1
        nums.reverse()


