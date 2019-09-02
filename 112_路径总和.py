# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if (root and not isinstance(root,TreeNode)) or not isinstance(sum,int):
            return None
        if not root:
            return None
        q = Queue()
        q.put((root,root.val))
        while not q.empty():
            cur_node,cur_val = q.get()
            if cur_node:
                left,right = cur_node.left,cur_node.right
                if left is None and right is None:
                    if cur_val == sum:
                        return True
                else:
                    if left:
                        q.put((left,cur_val+left.val))
                    if right:
                        q.put((right,cur_val+right.val))
        return False