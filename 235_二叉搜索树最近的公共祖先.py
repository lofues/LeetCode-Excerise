# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 共同的祖先必须两者值的闭区间中
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = root.left if p.val < root.val else root.right
        return root
