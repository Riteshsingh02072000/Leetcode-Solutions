class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        if n/3 > limit: return 0
        res = 0
        for k in range(limit+1):
            if (n-k)/2 > limit: continue
            m = n-k
            res += max(min(m,limit) - max((m-limit,0)) + 1, 0)
        return res
