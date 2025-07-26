class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mod = 10**9 + 7

        @lru_cache(None)

        def helper(idx, prev, prevFreq):
            if idx == n:
                return 1
            
            ans = 0
            for i in range(1, 7):
                if i == prev:
                    if prevFreq<rollMax[i-1]:
                        ans += helper(idx+1, i, prevFreq + 1)
                else:
                    ans += helper(idx+1, i, 1)
            
            return ans%mod
        return helper(0, 0, 0)