class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        ans = [0]*len(queries)
        sorted_queries =sorted([(q, i) for i, q in enumerate(queries)])

        heap = []
        count = 0
        visited = [[False]*n for _ in range(m)]
        heapq.heappush(heap, (grid[0][0], 0, 0))
        visited[0][0] = True
        direction = [0, 1, 0, -1, 0]

        for val, qi in sorted_queries:
            while heap and heap[0][0]<val:
                ele, i, j = heapq.heappop(heap)
                count += 1
                for x in range(4):
                    nr = i + direction[x]
                    nc = j + direction[x+1]
                    if 0<=nr<m and 0<=nc<n and not visited[nr][nc]:
                        visited[nr][nc] = True
                        heapq.heappush(heap, (grid[nr][nc], nr, nc))
            ans[qi] = count
        return ans
        