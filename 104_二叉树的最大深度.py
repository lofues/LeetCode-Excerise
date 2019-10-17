# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache
class Solution:
    @lru_cache(None)
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        return max(self.maxDepth(root.left),self.maxDepth(root.right))+1