"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloneMap = {}
        def clone(node):
            if node in cloneMap:
                return cloneMap[node]
            
            node_clone = Node(node.val, [])
            cloneMap[node] = node_clone

            for ngbr in node.neighbors:
                cloneMap[node].neighbors.append(clone(ngbr))
            return node_clone
        
        return clone(node) if node else None