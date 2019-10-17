# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if (root and not isinstance(root, TreeNode)) or not isinstance(sum, int):
            return None
        if not root:
            return []

        ret = []
        stack = [(root, [root.val])]
        while stack:
            cur_node, cur_path = stack.pop()
            left, right = cur_node.left, cur_node.right

            cur_sum = 0
            for item in cur_path:
                cur_sum += item

            if (cur_sum == sum) and (left is None and right is None):
                ret.append(cur_path)
            else:
                if right:
                    stack.append((right, cur_path + [right.val]))
                if left:
                    stack.append((left, cur_path + [left.val]))

        return ret