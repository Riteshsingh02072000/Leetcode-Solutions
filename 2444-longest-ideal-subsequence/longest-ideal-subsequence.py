class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0]*26

        for c in s:
            i = ord(c) - ord('a')
            dp[i] = 1 + self.getMax(dp, i, k)
        return max(dp)


    def getMax(self, dp, i, k):
        first = max(0, i-k)
        last = min(25, i+k)
        maxReach = 0
        for x in range(first, last+1):
            maxReach = max(maxReach, dp[x])
        return maxReach
        