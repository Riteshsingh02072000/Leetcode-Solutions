class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        mod = 12345
        m, n = len(grid), len(grid[0])
        ans = [[0]*n for i in range(m)]

        prefix = [1]
        suffix = 1

        for row in grid:
            for x in row:
                prefix.append(prefix[-1]*x%mod)
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                ans[i][j] = prefix[i*n+j]*suffix%mod
                suffix = suffix*grid[i][j] %mod
        return ans

        
        
        
        
        # nums = []
        # r, c = len(grid), len(grid[0])
        # mod = 12345
        # for x in grid:
        #     nums += x
        
        # n = len(nums)
        # ans = [0]*n
        # prefix = 1

        # for i in range(n):
        #     ans[i] = prefix
        #     prefix*=nums[i]
        
        # suffix = 1
        # for i in range(n-1, -1, -1):
        #     ans[i]*=suffix
        #     suffix*=nums[i]
        # ans = [x%mod for x in ans]
        
        # return [ans[i*c:(i+1)*c] for i in range(r)]

        # print(ans)