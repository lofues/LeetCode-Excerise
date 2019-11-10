class Solution(object):
    def findPeakElement(self, nums):
        """
        采用二分法确定峰值所在位置。

            如果当前nums[i]>nums[i-1] and nums[i]>nums[i+1] ，说明当前就是峰值。
            如果当前值小于前一个值，说明左边必有峰值。
            如果当前值小于后一个值，说明右边必有峰值
        """
        nums = [float('-inf')] + nums + [float('-inf')]
        left = 0
        right = len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[mid-1]  and nums[mid] > nums[mid+1]:
                return mid-1
            elif nums[mid] < nums[mid-1]:
                right = mid-1
            else:
                left = mid + 1
        # 遍历到left == right
        return left - 1