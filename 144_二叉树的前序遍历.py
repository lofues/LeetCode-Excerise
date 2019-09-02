# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return ret