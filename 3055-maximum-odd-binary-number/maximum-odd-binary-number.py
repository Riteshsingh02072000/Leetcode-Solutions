class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        n = len(s)
        ans = ''
        count = s.count('1')
        ans += '1'*(count-1)

        ans+='0'*(n-count)
        ans += '1'
        return ans