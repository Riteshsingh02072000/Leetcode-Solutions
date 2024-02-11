class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        # rows, cols = len(grid), len(grid[0])
        # cache = {}

        # def dfs(r, c1, c2):
        #     if (r, c1, c2) in cache:
        #         return cache[(r, c1, c2)]
        #     if c1==c2 or min(c1, c2)<0 or max(c1, c2)==cols:
        #         return 0
        #     if r == rows-1:
        #         return grid[r][c1] + grid[r][c2]
        #     ans = 0
        #     for c1_d, c2_d in product([-1,0, 1], [-1, 0, 1]):
        #         ans = max(ans, dfs(r+1, c1+c1_d, c2+c2_d))
        #     cache[(r, c1, c2)] = ans + grid[r][c1] + grid[r][c2]

        #     return cache[(r, c1, c2)]
        # return dfs(0, 0, cols-1)

        rows , cols = len(grid), len(grid[0])
        dp = [[0]*cols for _ in range(cols)]

        for r in reversed(range(rows)):
            cur_dp = [[0]*cols for _ in range(cols)]
            for c1 in range(cols-1):
                for c2 in range(c1+1, cols):
                    ans = 0
                    cherry = grid[r][c1] + grid[r][c2]

                    for c1_d, c2_d in product([-1,0,1], [-1,0,1]):
                        nc1, nc2 = c1+c1_d, c2+c2_d

                        if nc1<0 or nc2==cols:
                            continue
                        ans = max(ans, cherry+dp[nc1][nc2])
                    
                    cur_dp[c1][c2] = ans
            dp = cur_dp
        return dp[0][cols-1]

