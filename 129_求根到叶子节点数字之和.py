# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root and not isinstance(root,TreeNode):
            return True
        if not root:
            return 0
        ret = 0
        q = [(root,str(root.val))]
        while q:
            cur_node,cur_str = q.pop(0)
            if cur_node:
                left,right = cur_node.left,cur_node.right
                if left is None and right is None:
                    ret += int(cur_str)
                else:
                    if left:
                        q.append((left,cur_str+str(left.val)))
                    if right:
                        q.append((right,cur_str+str(right.val)))
        return ret