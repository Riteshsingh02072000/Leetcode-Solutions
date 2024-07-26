class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] =0
        
        for u, v, w in edges:
            dist[u][v] = dist[v][u] = w
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        minReachable = float('inf')
        ans = 0

        for i in range(n):
            reachable = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    reachable +=1
                
            if reachable<=minReachable:
                minReachable = reachable
                ans = i
        return ans
            
