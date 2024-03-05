class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j= len(s)-1
        while i<j and s[i]==s[j]:
            tmp = s[i]
            while i<len(s) and s[i]==tmp:
                i+=1
            while j>0 and s[j] == tmp:
                j-=1
        
        if j<i:
            return 0
        
        else:
            return j-i+1