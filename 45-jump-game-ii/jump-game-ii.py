class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')]*n
        dp[0] = 0

        for i in range(n):
            for j in range(nums[i]):
                if i+j+1<n:
                    dp[i+j+1]  = min(dp[i+j+1], 1+dp[i])
        return dp[-1]