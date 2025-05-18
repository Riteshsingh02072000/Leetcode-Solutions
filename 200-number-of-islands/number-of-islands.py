class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        direction = [0, 1, 0, -1, 0]
        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        
        def islandTraverse(i, j):
            grid[i][j] = 'V'
            for x in range(4):
                nr = i+direction[x]
                nc = j+direction[x+1]

                if inBound(nr, nc) and grid[nr][nc] == '1':
                    islandTraverse(nr, nc)
                    
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islandTraverse(i, j)
                    count += 1
        return count