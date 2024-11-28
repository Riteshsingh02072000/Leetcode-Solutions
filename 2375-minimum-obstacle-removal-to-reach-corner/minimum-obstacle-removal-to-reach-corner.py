class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        directions = (0, 1, 0, -1, 0)

        q = deque([(0, 0, 0)])
        visited = [[False]*n for _ in range(m)]
        visited[0][0] = True

        while q:
            x, y, removed = q.popleft()

            if x == m-1 and y == n-1:
                return removed
            
            for i in range(4):
                nx, ny = x+directions[i], y + directions[i+1]

                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    if grid[nx][ny] == 0:
                        q.appendleft((nx, ny, removed))
                    else:
                        q.append((nx, ny, removed+1))
        return -1
