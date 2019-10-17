# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None:
            return True
        elif root and root.left is None and root.right is None:
            return True
        elif root and root.left and root.right:
            return root.val == root.left.val and root.val == root.right.val and self.isUnivalTree(
                root.left) and self.isUnivalTree(root.right)
        elif root and root.left:
            return root.val == root.left.val and self.isUnivalTree(root.left)
        else:
            return root.val == root.right.val and self.isUnivalTree(root.right)

