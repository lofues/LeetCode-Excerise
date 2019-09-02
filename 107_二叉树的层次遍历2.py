# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root and not isinstance(root,TreeNode):
            return None
        if root is None:
            return []
        ret = []
        q = Queue()
        q.put((root,1))
        while not q.empty():
            cur_node,cur_level = q.get()
            if cur_node:
                if cur_level > len(ret):
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                q.put((cur_node.left,cur_level+1))
                q.put((cur_node.right,cur_level+1))
        return ret[::-1]