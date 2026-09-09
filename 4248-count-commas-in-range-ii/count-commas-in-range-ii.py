class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        p =1000
        while p<=n:
            count += n-p+1
            p*=1000
        return count