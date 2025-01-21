class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_right = sum(grid[0])
        bottom_left = 0
        ans = float('inf')

        for i in range(len(grid[0])):
            top_right -= grid[0][i]
            ans = min(ans, max(top_right, bottom_left))
            bottom_left += grid[1][i]
        return ans