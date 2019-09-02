# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import Queue

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return 0
        q = Queue()
        ret = []
        q.put((root,1))
        while not q.empty():
            cur_node,cur_level = q.get()
            if cur_node:
                q.put((cur_node.left,cur_level+1))
                q.put((cur_node.right,cur_level+1))
                if cur_node.left is None and cur_node.right is None:
                    if cur_level not in ret:
                        ret.append(cur_level)
        return ret[0]