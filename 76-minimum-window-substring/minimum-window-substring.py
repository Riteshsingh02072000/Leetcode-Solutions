class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        if t=="":
            return ""
        countT = collections.defaultdict(int)
        window = collections.defaultdict(int)
        for x in t:
            countT[x]+=1
        # print(countT)
        need = len(countT)
        have =  0
        print(have)
        l = 0
        res = [-1, -1]
        length = float('inf')

        for r in range(len(s)):
            c = s[r]
            window[c] +=1

            if c in countT and window[c]==countT[c]:
                have +=1
            
            while have==need:
                
                if (r-l+1)<length:
                    res = [l,r]
                    length = r-l+1
                
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r = res
        return s[l:r+1] if length!=float('inf') else ""