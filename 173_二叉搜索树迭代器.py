# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        if root is None:
            self.ret = []
        else:
            self.ret = self.in_order(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.ret.pop(0)

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.ret)

    def in_order(self, root):
        if root is None:
            return []
        else:
            ret = []
            ret.extend(self.in_order(root.left))
            ret.append(root.val)
            ret.extend(self.in_order(root.right))
            return ret

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()