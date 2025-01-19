class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]

        heap = []

        for i in range(m):
            for j in [0, n-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
            
        for j in range(n):
            for i in [0, m-1]:
                heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        # def inBound(i)
        # print(heap)
        ans = 0
        directions = [0, 1, 0, -1, 0]

        while heap:
            height, i, j = heappop(heap)
            for x in range(4):
                ni, nj = i+ directions[x], j+directions[x+1]
                if 0<=ni<m and 0<=nj<n and not visited[ni][nj]:
                    ans += max(0, height-heightMap[ni][nj])
                    heappush(heap, (max(height, heightMap[ni][nj]), ni, nj))
                    visited[ni][nj] = True
        return ans
