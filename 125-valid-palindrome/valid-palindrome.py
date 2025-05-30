class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [x.lower() for x in s if x.isalnum()]
        # print(s)
        l =0
        r = len(s)-1

        while l<=r:
            if s[l]!=s[r]:
                return False
            else:
                l += 1
                r-=1
        return True
