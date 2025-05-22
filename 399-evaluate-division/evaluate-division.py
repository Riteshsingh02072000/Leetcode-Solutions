class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def dfs(src, dst, val):
            q = deque([[src, val]])
            visited = set()

            while q:
                node, val = q.popleft()
                if node == dst:
                    return val
                if node in visited:
                    continue

                visited.add(node)
                for ngbr in graph[node]:
                    if ngbr not in visited:
                        q.append([ngbr, val*graph[node][ngbr]])
            return float(-1)
        
        graph = defaultdict(dict)
        for i in range(len(values)):
            u, v = equations[i]
            val = values[i]
            graph[u][v] = val
            graph[v][u] = 1/val
        
        ans = []
        for a,b in queries:
            if a not in graph or b not in graph:
                ans.append(float(-1))
            else:
                res = dfs(a, b, 1)
                ans.append(res)
        return ans
