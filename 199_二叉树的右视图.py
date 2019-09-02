# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root and not isinstance(root, TreeNode):
            return None
        if not root:
            return []
        ret = []
        level = 0
        q = [(root, 1)]
        while q:
            cur_node, cur_level = q.pop(0)
            left, right = cur_node.left, cur_node.right
            if cur_node:
                if cur_level > level:
                    level = cur_level
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                if left:
                    q.append((left, cur_level + 1))
                if right:
                    q.append((right, cur_level + 1))
        return [x[-1] for x in ret]



