class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 1: return -1
        left,right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            # 找出left = mid + 1的条件 其余均为 right = mid - 1
            # 当[0,mid] 为有序时
            elif nums[mid] >= nums[0] and (target < nums[0] or nums[mid] < target):
                left = mid + 1
            # 当[0,mid] 为无序时
            elif nums[mid] < nums[0] and (target < nums[0] and nums[mid] < target):
                left = mid + 1
            else:
                right = mid - 1
        return left if left == right and nums[left] == target else -1
