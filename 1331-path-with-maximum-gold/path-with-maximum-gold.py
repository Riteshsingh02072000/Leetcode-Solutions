class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = set()

        def inBound(i, j):
            return 0<=i<n and 0<=j<m

        
        def dfs(row, col):
            if not inBound(row, col) or (row, col) in visited or grid[row][col] == 0:
                return 0
        
            visited.add((row, col))
            left = dfs(row, col-1)
            right = dfs(row, col+1)
            up = dfs(row-1, col)
            down = dfs(row+1, col)

            visited.remove((row, col))
            return grid[row][col] + max(left, right, up, down)
        
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0 and (i, j) not in visited:
                    ans = max(ans, dfs(i, j))
        return ans