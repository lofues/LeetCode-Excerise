# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        min1,min2=float('inf'),float('inf')
        def f(r):
            if r:
                nonlocal min1,min2
                if r.val>min1:
                    if r.val<min2:
                        min2=r.val
                else:
                    if min2>float('inf'):
                        min2=min1
                    min1=r.val
                f(r.left)
                f(r.right)
        f(root)
        if min2!=float('inf'):
            return min2
        else:
            return -1
