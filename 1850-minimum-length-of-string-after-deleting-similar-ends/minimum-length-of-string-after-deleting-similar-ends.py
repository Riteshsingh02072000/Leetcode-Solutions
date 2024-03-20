class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) -1

        while l<r and s[l] == s[r]:
            tmp = s[l]

            while l<len(s) and s[l]==tmp:
                l+=1

            while r>0 and s[r]==tmp:
                r-=1
        if r<l:
            return 0
        else:
            return r-l+1