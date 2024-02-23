"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        graph = {}

        def dfs(node):
            if not node:
                return None
            if node in graph:
                return graph[node]
            
            graph[node] = ListNode(node.val)
            graph[node].next = dfs(node.next)
            graph[node].random = dfs(node.random)

            return graph[node]
        return dfs(head)