# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:root_index+1],inorder[0:root_index])
        root.right = self.buildTree(preorder[root_index+1:],inorder[root_index+1:])
        return root