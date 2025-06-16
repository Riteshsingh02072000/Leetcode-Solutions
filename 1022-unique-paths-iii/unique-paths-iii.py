class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        start = None
        count = 0
        directions = [0, 1, 0, -1, 0]
        for i in range(m):
            for j in range(n):
                count += grid[i][j] == 0
                if grid[i][j] == 1:
                    start = (i, j)
        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        def backTrack(i, j):
            result = 0
            nonlocal count
            for x in range(4):
                nr = i+directions[x]
                nc = j+directions[x+1]
                if inBound(nr, nc):
                    if grid[nr][nc] == 0:
                        count -= 1
                        grid[nr][nc] = -1
                        result += backTrack(nr, nc)
                        count += 1
                        grid[nr][nc] = 0
                    elif grid[nr][nc] == 2:
                        result += count == 0
            return result
        return backTrack(start[0], start[1])
