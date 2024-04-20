class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        graph = {i: [] for i in range(n)}
        for u, v, length in edges:
            graph[u].append((v, length))
            graph[v].append((u, length))

        res = [-1] * n
        pq = [(0, 0)] 
        while pq:
            time, node = heapq.heappop(pq)
            if res[node] != -1:  
                continue
            res[node] = time
            for neighbor, edge_length in graph[node]:
                if res[neighbor] == -1 and time + edge_length < disappear[neighbor]:
                    heapq.heappush(pq, (time + edge_length, neighbor))

        return res