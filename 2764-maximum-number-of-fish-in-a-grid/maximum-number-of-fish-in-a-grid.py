class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        m, n  = len(grid), len(grid[0])
        ans = 0
        direction = [0, 1, 0, -1, 0]
        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        def helper(i, j):
            fish = 0
            if grid[i][j] == 0:
                return fish
            
            fish += grid[i][j]
            grid[i][j] = -1

            for x in range(4):
                nr = i+direction[x]
                nc = j+direction[x+1]
                if inBound(nr, nc) and grid[nr][nc]>0:
                    fish+=helper(nr, nc)
            return fish
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]>0:
                    ans = max(ans, helper(i, j))
        return ans