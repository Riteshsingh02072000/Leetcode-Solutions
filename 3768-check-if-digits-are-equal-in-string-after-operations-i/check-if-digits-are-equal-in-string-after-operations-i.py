class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            n = len(s)
            tmp = ""
            for i in range(n-1):
                tmp += str((int(s[i])+ int(s[i+1]))%10)
            s = tmp
        return s[0] == s[1]