class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        words = set(dictionary)
        
        dp = [i for i in range(n+1)]
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            for l in range(1, i+1):
                if s[i-l:i] in words:
                    dp[i] = min(dp[i], dp[i-l])
        return dp[-1]