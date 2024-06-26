class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans += self.helper(s, i, i)
            ans+=self.helper(s, i, i+1)
        return ans
    def helper(self, s, l, r):
        count = 0
        while l>=0 and r<len(s) and s[l]==s[r]:
            count +=1
            l-=1
            r+=1
        return count