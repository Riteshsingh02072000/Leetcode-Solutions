class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dp(pos):
            if pos<0:
                return 0
            if pos ==0:
                return nums[0]
            if pos in memo:
                return memo[pos]
            
            memo[pos] = max(dp(pos-1), dp(pos-2)+nums[pos])
            print(memo[pos])

            return memo[pos]
        return dp(len(nums)-1)