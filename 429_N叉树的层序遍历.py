"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root and not isinstance(root,Node):
            return None
        if root is None:
            return []
        ret = []
        queue = [(root,1)]
        while queue:
            cur_node,level = queue.pop(0)
            if cur_node:
                if level > len(ret):
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                if cur_node.children:
                    for item in cur_node.children:
                        queue.append((item,level+1))
        return ret