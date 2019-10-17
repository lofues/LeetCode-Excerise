# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return []
        ret = []
        stack = [root.val, root.right, root.left]
        while stack:
            tmp = stack.pop()
            if tmp:
                if isinstance(tmp, TreeNode):
                    stack += [tmp.val, tmp.right, tmp.left]
                else:
                    ret.append(tmp)
        return ret
