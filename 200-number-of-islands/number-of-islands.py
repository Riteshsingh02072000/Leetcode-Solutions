class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        ans = 0
        direction = [0, 1, 0, -1, 0]

        def inBound(i, j):
            return 0<=i<n and 0<=j<m
        
        def dfs(i, j):
            # if not inBound(i, j):
            #     return 
            if grid[i][j]!='1':
                return
            
            grid[i][j] = 'V'
            for x in range(4):
                nr = i + direction[x]
                nc = j + direction[x+1]

                if inBound(nr, nc) and grid[nr][nc] == '1':
                    dfs(nr, nc)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
