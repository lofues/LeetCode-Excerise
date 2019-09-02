"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root and not isinstance(root,Node):
            return None
        if root is None:
            return []
        ret = []
        stack = [root]
        while stack:
            # root right left
            tmp = stack.pop()
            if tmp:
                ret.append(tmp.val)
                for item in tmp.children:
                    stack.append(item)
        return ret[::-1]