class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0,0
        if s == "":
            return True
        while l<len(s) and r<len(t):
            if s[l] == t[r]:
                if l==len(s)-1:
                    return True
                l+=1
                r+=1
            else:
                r+=1
        return False