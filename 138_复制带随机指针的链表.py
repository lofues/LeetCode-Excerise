"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # dfs
        seen = {}
        def dfs(node):
            if not node:
                return
            if node in seen:
                return seen[node]
            clone = Node(node.val,[])
            seen[node] = clone
            for n in node.neighbors:
                clone.neighbors.append(dfs(n))
            return clone
        return dfs(node)