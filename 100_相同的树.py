# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if (self.pre_order(p) == self.pre_order(q)) and (self.in_order(p) == self.in_order(q)):
            return True
        else:
            return False

    def pre_order(self, node):
        if node is None:
            return []
        else:
            ret = []
            ret.append(node.val)
            ret.extend(self.pre_order(node.left))
            ret.extend(self.pre_order(node.right))
            return ret

    def in_order(self, node):
        if node is None:
            return []
        else:
            ret = []
            ret.extend(self.in_order(node.left))
            ret.append(self.in_order(node.right))
            return ret