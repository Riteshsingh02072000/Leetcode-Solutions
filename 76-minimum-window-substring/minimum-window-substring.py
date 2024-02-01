class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t) or t == "":
            return ""
        
        countT = defaultdict(int)
        window = defaultdict(int)

        for x in t:
            countT[x]+=1
        
        need = len(countT)
        have = 0

        length = float('inf')
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c]+=1
            if c in countT and countT[c] == window[c]:
                have +=1
            while have==need:
                if r-l+1<length:
                    length = r-l+1
                    res = [l,r]
                
                window[s[l]]-=1
                if s[l] in countT and countT[s[l]]>window[s[l]]:
                    have -= 1
                l+=1
        l, r = res
        return s[l:r+1] if length!=float('inf') else ""




        # if len(s)<len(t) or t=="":
        #     return ""
        
        # countT = collections.defaultdict(int)
        # window = collections.defaultdict(int)

        # for x in t:
        #     countT[x] +=1
        
        # need = len(countT)
        # have = 0 

        # length = float('inf')
        # l = 0
        # res = [-1, -1]

        # for r in range(len(s)):
        #     c = s[r]
        #     window[c] +=1

        #     if c in countT and countT[c] == window[c]:
        #         have +=1
            
        #     while have==need:
        #         if r-l+1<length:
        #             length = r-l+1
        #             res = [l, r]
                
        #         window[s[l]] -=1
        #         if s[l] in countT and window[s[l]]<countT[s[l]]:
        #             have -= 1

        #         l+=1
        # l,  r = res
        # return s[l:r+1] if length!=float('inf') else ""
