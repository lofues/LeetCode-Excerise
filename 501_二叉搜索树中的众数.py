# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root and not isinstance(root, TreeNode):
            return None
        if root is None:
            return []
        d = {}
        ret = []
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node:
                if node.val not in d:
                    d[node.val] = 1
                else:
                    d[node.val] += 1
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        max_num = sorted(d.items(), key=lambda x: x[1], reverse=True)[0][1]
        for k, v in sorted(d.items(), key=lambda x: x[1], reverse=True):
            if v == max_num:
                ret.append(k)
        return ret
