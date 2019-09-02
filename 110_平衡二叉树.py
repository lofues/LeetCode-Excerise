# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache


class Solution:
    @lru_cache(maxsize=None)
    def parse_height(self, root):
        if root is None:
            return 0
        if root and root.left is None and root.right is None:
            return 1
        return max(self.parse_height(root.left), self.parse_height(root.right)) + 1

    @lru_cache(maxsize=None)
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        return abs(self.parse_height(root.left) - self.parse_height(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)
