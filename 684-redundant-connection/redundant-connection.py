class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        visited = set()

        def dfs(node, path, prev):
            if node in visited:
                return (True, path)
            visited.add(node)
            for ngbr in graph[node]:
                if ngbr == prev:
                    continue
                cycle, new_path = dfs(ngbr, path + [ngbr], node)
                if cycle:
                    return (True, new_path)
            return (False, [])
        

        _, path = dfs(1, [1], -1)
        for i in range(len(path)):
            if path[i] == path[-1]:
                path = path[i:]
                break
        
        for i in range(len(edges)-1, -1, -1):
            if edges[i][0] in path and edges[i][1] in path:
                return edges[i]