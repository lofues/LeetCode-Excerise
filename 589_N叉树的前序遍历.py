"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root and not isinstance(root,Node):
            return None
        if root is None:
            return []
        stack = [root]
        ret = []
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                if node.children:
                    for item in node.children[::-1]:
                        stack.append(item)
        return ret