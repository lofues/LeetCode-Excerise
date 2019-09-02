# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.IsSymmetric(root.left, root.right)

    def IsSymmetric(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        elif node1 is None or node2 is None:
            return False
        else:
            return (node1.val == node2.val) and (self.IsSymmetric(node1.left, node2.right)) and (
                self.IsSymmetric(node1.right, node2.left))