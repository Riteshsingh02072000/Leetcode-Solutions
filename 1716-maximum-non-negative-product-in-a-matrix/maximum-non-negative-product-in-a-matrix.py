class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7 
        dpMax = [[0]*n for i in range(m)]
        dpMin = [[0]*n for i in range(m)]

        dpMax[0][0] = grid[0][0]
        dpMin[0][0] = grid[0][0]
        


        for j in range(1, n):
            dpMax[0][j] = dpMax[0][j-1]*grid[0][j]
            dpMin[0][j] = dpMax[0][j]

        for i in range(1, m):
            dpMax[i][0] = dpMax[i-1][0]*grid[i][0]
            dpMin[i][0] = dpMax[i][0]
        
        for i in range(1, m):
            for j in range(1, n):
                val = grid[i][j]
                options = [
                    dpMax[i-1][j]*val,
                    dpMin[i-1][j]*val,
                    dpMax[i][j-1]*val,
                    dpMin[i][j-1]*val
                ]
                dpMax[i][j] = max(options)
                dpMin[i][j] = min(options)
        
        ans = dpMax[m-1][n-1]
        return ans%mod if ans>=0 else -1

       
        # def inBound(i, j):
        #     return 0<=i<m and 0<=j<n
        # def dfs(row, col, prod):
        #     if not inBound(row, col):
        #         return
        #     if row==m-1 and col==n-1:
        #         if prod*grid[row][col]>ans:
        #             ans = prod*grid[row][col]
        #         return
            
        #     prod*= grid[row][col]
        #     dfs(row+1, col, prod)
        #     dfs(row, col+1, prod)
        # dfs(0, 0, 1)
        # return ans%(10**9+7) if ans>0 else -1
