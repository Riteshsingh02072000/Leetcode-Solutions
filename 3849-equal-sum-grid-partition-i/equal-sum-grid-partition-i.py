class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        sumRow = [0]*m
        sumCol = [0]*n

        for i in range(m):
            sumRow[i] = sum(grid[i])
            
        
        for j in range(n):
            for i in range(m):
                sumCol[j] += grid[i][j]
        
        total = sum(sumRow)
        prefix = 0

        for i in range(1, m):
            prefix += sumRow[i-1]
            if prefix == total-prefix:
                return True
        
        total = sum(sumCol)
        prefix = 0

        
        for j in range(1, n):
            prefix += sumCol[j-1]
            if prefix == total - prefix:
                return True
        
        return False