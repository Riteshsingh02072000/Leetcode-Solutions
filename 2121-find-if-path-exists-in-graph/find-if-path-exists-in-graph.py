class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(node, visited):
            if node == destination:
                return True
            visited.add(node)
            for ngbr in graph[node]:
                if ngbr not in visited:
                    if dfs(ngbr, visited):
                        return True
            return False
        visited = set()
        # q= deque([source])
        # while q:
        #     node = q.popleft()
        #     if node == destination:
        #         return True
            
        #     visited.add(node)
        #     for ngbr in graph[node]:
        #         if ngbr in visited:
        #             continue
        #         q.append(ngbr)
        return dfs(source, visited)