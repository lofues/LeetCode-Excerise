
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return None
        queue = [(root,1)]
        ret_list = []
        while queue:
            cur_node,cur_level = queue.pop(0)
            if cur_node:
                left,right = cur_node.left,cur_node.right
                if len(ret_list) < cur_level:
                    ret_list.append([cur_node.val])
                else:
                    ret_list[-1].append(cur_node.val)
                if left:
                    queue.append((left,cur_level + 1))
                if right:
                    queue.append((right,cur_level + 1))
        return [max(x) for x in ret_list]