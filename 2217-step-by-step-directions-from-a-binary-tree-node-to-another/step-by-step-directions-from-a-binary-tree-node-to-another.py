# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        adj = defaultdict(list)

        def dfs(node):
            if not node:
                return 
            
            if node.left:
                adj[node.val].append((node.left.val, "L"))
                adj[node.left.val].append((node.val, "U"))
                dfs(node.left)
            if node.right:
                adj[node.val].append((node.right.val, "R"))
                adj[node.right.val].append((node.val, "U"))
                dfs(node.right)
        
        dfs(root)

        q = deque()
        q.append((startValue, ""))
        visited = set([startValue])

        while q:
            for i in range(len(q)):
                node, s = q.popleft()
                if node == destValue:
                    return s
                
                for child, st in adj[node]:
                    if child not in visited:
                        visited.add(child)
                        q.append((child, s+st))
                        