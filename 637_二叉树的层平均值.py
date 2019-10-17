# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return []
        ret = []
        queue = [(root,1)]
        while queue:
            cur_node,level = queue.pop(0)
            if cur_node:
                left,right = cur_node.left,cur_node.right
                if level > len(ret):
                    ret.append([cur_node.val])
                else:
                    ret[-1].append(cur_node.val)
                if left:
                    queue.append((left,level+1))
                if right:
                    queue.append((right,level+1))
        return [sum(x)/len(x) for x in ret]