# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root and not isinstance(root, TreeNode):
            return None
        if root is None:
            return 0
        ret = self.in_order(root)
        ans = [x for x in ret if x >= L and x <= R]
        return sum(ans)

    def in_order(self, root):
        if root is None:
            return []
        ret = []
        ret.extend(self.in_order(root.left))
        ret.append(root.val)
        ret.extend(self.in_order(root.right))
        return ret