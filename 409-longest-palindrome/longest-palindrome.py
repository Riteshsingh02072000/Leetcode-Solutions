class Solution:
    def longestPalindrome(self, s: str) -> int:
        pld = set()
        ans = 0
        for i in s:
            if i in pld:
                pld.remove(i)
                ans+=1
            else:
                pld.add(i)
        
        if len(pld) != 0:
            return ans*2 +1
        return ans*2