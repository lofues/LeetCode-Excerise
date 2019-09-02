# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return None
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        ret.sort()
        ans = ret[-1]
        for i, v in enumerate(ret):
            if i < len(ret) - 1 and ret[i + 1] - ret[i] < ans:
                ans = ret[i + 1] - ret[i]
        return ans
