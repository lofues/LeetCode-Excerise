# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return 0

        def is_leaf(node):
            if node is None:
                return False
            return node.left is None and node.right is None

        q = [root]
        ret = 0
        while q:
            node = q.pop(0)
            if node:
                if node.left and is_leaf(node.left):
                    ret += node.left.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ret


