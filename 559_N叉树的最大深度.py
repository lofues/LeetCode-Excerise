"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        elif self.is_leaf(root):
            return 1
        else:
            return max(self.maxDepth(item) for item in root.children) + 1

    def is_leaf(self, root):
        return not root.children