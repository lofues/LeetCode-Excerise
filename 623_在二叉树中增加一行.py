# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if root and not isinstance(root, TreeNode):
            return None
        if not root or d == 1:
            node = TreeNode(v)
            node.left = root
            return node

        queue = [(root, 1)]
        while queue:
            cur_node, cur_level = queue.pop(0)
            if cur_node:
                left, right = cur_node.left, cur_node.right
                if (cur_level == d - 1):
                    tmp = TreeNode(v)
                    tmp1 = TreeNode(v)
                    tmp.left = left
                    tmp1.right = right

                    cur_node.left = tmp
                    cur_node.right = tmp1
                    queue.append((left, cur_level + 2))
                    queue.append((right, cur_level + 2))
                else:
                    if left:
                        queue.append((left, cur_level + 1))
                    if right:
                        queue.append((right, cur_level + 1))
        return root


