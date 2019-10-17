# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return []
        ret = []
        tup_list = []
        q = Queue()
        q.put((root, 1))
        while not q.empty():
            cur_node, cur_level = q.get()
            if cur_node:
                q.put((cur_node.left, cur_level + 1))
                q.put((cur_node.right, cur_level + 1))
                tup_list.append((cur_node.val, cur_level))
        for val, level in tup_list:
            if level > len(ret):
                ret.append([val])
            else:
                ret[-1].append(val)
        return ret

