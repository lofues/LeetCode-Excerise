# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return False
        sort_list = self.in_order(root)
        for item in sort_list:
            if k - item in sort_list and k - item != item:
                return True
        return False

    def in_order(self, root):
        if not root:
            return []
        ret = []
        ret.extend(self.in_order(root.left))
        ret.append(root.val)
        ret.extend(self.in_order(root.right))
        return ret