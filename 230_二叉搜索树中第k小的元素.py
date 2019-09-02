# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from functools import lru_cache


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return None

        @lru_cache(maxsize=None)
        def in_order(root):
            if not root:
                return []
            if root:
                ret = []
                ret.extend(in_order(root.left))
                ret.append(root.val)
                ret.extend(in_order(root.right))
                return ret

        return in_order(root)[k - 1]