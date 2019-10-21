# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s is None and t is None:
            return True
        elif s is None:
            return False

        return self.is_equal(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def is_equal(self, tree1, tree2):
        if tree2 is None and tree1 is None:
            return True
        elif tree1 is None or tree2 is None:
            return False

        return tree1.val == tree2.val and self.is_equal(tree1.left, tree2.left) and self.is_equal(tree1.right,
                                                                                                  tree2.right)
