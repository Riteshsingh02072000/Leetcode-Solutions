# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def dfs(node):
            if not node:
                return 
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        graph = collections.defaultdict(list)
        dfs(root)
        time = -1
        q = deque([start])
        visited = set()

        while q:
            time+=1
            for _ in range(len(q)):
                cur = q.popleft()
                visited.add(cur)

                for ngbr in graph[cur]:
                    if ngbr not in visited:
                        q.append(ngbr)
        return time