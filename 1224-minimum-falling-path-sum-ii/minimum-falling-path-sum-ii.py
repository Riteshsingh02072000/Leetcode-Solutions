class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dp = [[-1]*m for _ in range(n)]
        ans = float('inf')

        for j in range(m):
            dp[0][j] = grid[0][j]
        
        for i in range(1, n):
            for j in range(m):
                tmp = float('inf')
                for k in range(m):
                    if j!=k:
                        tmp = min(tmp, grid[i][j]+dp[i-1][k])
                dp[i][j] = tmp
        for j in range(m):
            ans = min(ans, dp[n-1][j])
        return ans