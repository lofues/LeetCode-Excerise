class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        先找出最大的索引 k 满足 nums[k] < nums[k+1]，如果不存在，就翻转整个数组；
        再找出另一个最大索引 l 满足 nums[l] > nums[k]；
        交换 nums[l] 和 nums[k]；
        最后翻转 nums[k+1:]。
        """
        if len(nums) < 2:
            return
        k = len(nums) - 2
        for k in range(len(nums) - 2, -1, -1):
            if nums[k] < nums[k + 1]:
                break
        # 判断是否无满足的k
        if nums[k] >= nums[k + 1]:
            nums.reverse()
            return
        # 找到最大的i 有nums[i] > nums[k]
        i = len(nums) - 1
        for i in range(len(nums) - 1, k, -1):
            if nums[i] > nums[k]:
                break
        # swap nums[i] and nums[k]
        nums[k], nums[i] = nums[i], nums[k]
        # reverse nums[k+1:]
        nums[k + 1:] = nums[:k:-1]
