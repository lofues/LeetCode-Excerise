# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root and not isinstance(root,TreeNode):
            return None
        if not root:
            return []
        paths = []
        q = [(root,str(root.val))]
        while q:
            cur_node,path = q.pop(0)
            left,right = cur_node.left,cur_node.right
            if cur_node:
                if left is None and right is None:
                    paths.append(path)
                if left:
                    q.append((left,path + '->' + str(left.val)))
                if right:
                    q.append((right,path + '->' +  str(right.val)))
        return paths