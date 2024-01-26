class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        memo = {}
        mod = 10**9 +7

        def dfs(i, j, moves):
            if (i, j, moves) in memo:
                return memo[(i, j, moves)]
            
            elif i<0 or j <0 or i>=m or j>=n:
                return 1
            
            elif moves == 0:
                return 0
            
            ans = dfs(i+1, j, moves-1)
            ans+=dfs(i-1, j, moves-1)
            ans+=dfs(i, j-1, moves-1)
            ans+= dfs(i, j+1, moves-1)

            memo[(i, j, moves)] = ans
            return ans
        
        return dfs(startRow, startColumn, maxMove) % mod