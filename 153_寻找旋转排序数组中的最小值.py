class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        low,high = 0,len(nums)-1
        if nums[high] > nums[low]: return nums[low]
        while low <= high:
            mid = low + (high-low) // 2
            if nums[mid] > nums[0]:
                low = mid
            elif nums[mid] < nums[0]:
                high = mid
            if nums[mid] > nums[mid+1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid-1]:
                return nums[mid]