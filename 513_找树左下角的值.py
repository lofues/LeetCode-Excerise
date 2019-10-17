# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return None
        queue = [(root,1)]
        ret = []
        while queue:
            cur_node,cur_level = queue.pop(0)
            left,right = cur_node.left,cur_node.right
            if len(ret) < cur_level:
                ret.append([cur_node.val])
            else:
                ret[-1].append(cur_node.val)
            if left:
                queue.append((left,cur_level+1))
            if right:
                queue.append((right,cur_level+1))
        return ret[-1][0]