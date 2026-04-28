class Solution:
    def minOperations(self, grid: List[List[int]], t: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = [grid[i][j] for j in range(n) for i in range(m)]
        
        base = arr[0]
        for x in arr:
            if abs(x-base)%t!=0:
                return -1
        arr.sort()
        median = arr[len(arr)//2]
        ans = 0
        for x in arr:
            ans += abs(x-median)//t
        
        return ans