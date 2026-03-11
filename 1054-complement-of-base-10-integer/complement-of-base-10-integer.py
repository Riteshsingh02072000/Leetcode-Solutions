class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        ans = 0
        factor = 1
        while (n>0):
            ans += factor*(1 if n%2==0 else 0)
            factor *= 2
            n//=2
        return ans