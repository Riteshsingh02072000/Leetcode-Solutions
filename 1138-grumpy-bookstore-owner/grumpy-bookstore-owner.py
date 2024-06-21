class Solution:
    def maxSatisfied(self, c: List[int], g: List[int], m: int) -> int:
        n = len(c)
        total = sum(c[:m])
        total += sum((1-g[i])*c[i] for i in range(m, n))

        ans = total

        for i in range(m, n):
            total -= g[i-m]*c[i-m]
            total+= g[i]*c[i]
            ans = max(ans, total)
        return ans
