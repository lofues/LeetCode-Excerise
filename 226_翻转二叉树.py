# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache

class Solution:
    @lru_cache(maxsize=None)
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return root
        if root.left or root.right:
            root.left,root.right = root.right,root.left
            root.left,root.right = self.invertTree(root.left),self.invertTree(root.right)
        return root