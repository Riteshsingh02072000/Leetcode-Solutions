class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for i in range(n)]
        graph = defaultdict(list)

        for u, v in edges:
            graph[v].append(u)
        
        def dfs(node, curr):
            for v in graph[curr]:
                if v not in ans[node]:
                    dfs(node, v)
                    ans[node].append(v)
        
        for i in range(n):
            dfs(i, i)
        
        for k in ans:
            k.sort()
        return ans