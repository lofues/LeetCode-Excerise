# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_index = self.find_max_index(nums)
        root = TreeNode(nums[max_index])
        root.left = self.constructMaximumBinaryTree(nums[0:max_index])
        root.right = self.constructMaximumBinaryTree(nums[max_index + 1:])
        return root

    def find_max_index(self, nums):
        max_tmp = nums[0]
        max_index = 0
        for i, num in enumerate(nums):
            if num > max_tmp:
                max_tmp = num
                max_index = i
        return max_index