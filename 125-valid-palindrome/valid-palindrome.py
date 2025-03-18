class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join([x.lower() for x in list(s) if x.isalnum()])
        l, r = 0, len(s)-1
        n = len(s)
        while l<=r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if l>r or s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True