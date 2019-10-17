# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None
        node = root
        while node:
            if node.left:
                tmp = node.left
                while tmp.right:
                    tmp = tmp.right
                tmp.right = node.right
                node.right = node.left
                node.left = None
                node = node.right
            else:
                node = node.right
        return root