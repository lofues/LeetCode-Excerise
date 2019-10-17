# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root and not isinstance(root,TreeNode):
            return None
        if root is None:
            return TreeNode(val)
        node = root
        parent = None
        while node:
            parent = node
            node = node.left if val < node.val else node.right
        if val < parent.val:
            parent.left = TreeNode(val)
        else:
            parent.right = TreeNode(val)
        return root