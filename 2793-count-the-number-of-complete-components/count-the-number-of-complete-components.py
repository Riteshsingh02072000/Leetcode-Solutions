class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(v, res):
            if v in visit:
                return
            visit.add(v)
            res.append(v)
            for ngbr in adj[v]:
                dfs(ngbr, res)

            return res


        adj = defaultdict(list)
        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)
            
        ans = 0
        visit = set()

        for v in range(n):
            if v in visit:
                continue
            component = dfs(v, [])
            if all([len(component)-1 == len(adj[v2]) for v2 in component]):
                ans += 1
        return ans
