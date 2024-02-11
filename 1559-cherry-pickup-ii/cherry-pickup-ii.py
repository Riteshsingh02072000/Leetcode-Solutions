class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        cache = {}

        def dfs(r, c1, c2):
            if (r, c1, c2) in cache:
                return cache[(r, c1, c2)]
            if c1==c2 or min(c1, c2)<0 or max(c1, c2)==cols:
                return 0
            if r == rows-1:
                return grid[r][c1] + grid[r][c2]
            ans = 0
            for c1_d, c2_d in product([-1,0, 1], [-1, 0, 1]):
                ans = max(ans, dfs(r+1, c1+c1_d, c2+c2_d))
            cache[(r, c1, c2)] = ans + grid[r][c1] + grid[r][c2]

            return cache[(r, c1, c2)]
        return dfs(0, 0, cols-1)