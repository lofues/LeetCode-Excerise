# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def countNodes(self, root: TreeNode) -> int:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return 0
        return self.countNodes(root.left) + self.countNodes(root.right) + 1