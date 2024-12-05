class Solution:
    def canChange(self, s: str, t: str) -> bool:
        i, j = 0,0
        n = len(s)
        s += '#'
        t+='#'

        while i<n or j <n:
            while i<n and s[i] == '_': i+=1
            while j<n and t[j] == '_': j+=1

            if s[i]!=t[j]:
                return False
            if s[i] == 'L' and i<j:
                return False
            if s[i] == 'R' and i>j:
                return False
            i+=1
            j+=1
        return True