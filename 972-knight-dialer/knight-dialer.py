class Solution:
    def knightDialer(self, n: int) -> int:
        @lru_cache(None)
        def helper(n, row, col):
            if n==0:
                return 1
            ans = 0 
            for r, c in [[2,1], [1,2], [-2,1], [-1,2], [2,-1], [1,-2], [-2,-1], [-1,-2]]:
                nr = row+r
                nc = col+c
                if (-1<nr<3 and -1<nc<3) or (nr == 3 and nc==1):
                    ans+=helper(n-1, nr, nc)
            return ans%(10**9+7)
        
        ans = helper(n-1, 3,1)
        for i in range(3):
            for j in range(3):
                ans+=helper(n-1, i, j)
        return ans%(10**9+7)