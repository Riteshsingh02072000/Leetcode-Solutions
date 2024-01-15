class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join([x.lower() for x in s if x.isalnum()])
        # print(s)

        # return s == s[::-1]

        l = 0
        r = len(s)-1

        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            
            if l>r or s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1
        return True
