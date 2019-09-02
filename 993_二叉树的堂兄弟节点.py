# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root and not isinstance(root, TreeNode):
            return None
        if root is None:
            return False
        if x == y:
            return False
        if x == root.val or y == root.val:
            return False
        x_des, y_des = None, None
        stack = [(root, 1)]
        while stack:
            cur_node, level = stack.pop()
            if cur_node:
                left, right = cur_node.left, cur_node.right
                if right:
                    stack.append((right, level + 1))
                    if right.val == x:
                        x_des = (cur_node, level + 1)
                    if right.val == y:
                        y_des = (cur_node, level + 1)
                if left:
                    stack.append((left, level + 1))
                    if left.val == x:
                        x_des = (cur_node, level + 1)
                    if left.val == y:
                        y_des = (cur_node, level + 1)
            if x_des and y_des:
                break
        if x_des is None or y_des is None:
            return False
        return x_des[0] != y_des[0] and x_des[1] == y_des[1]
