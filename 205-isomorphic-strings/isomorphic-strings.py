class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = dict()
        if len(s)!= len(t) or len(set(s))!=len(set(t)):
            return False
        
        for i, x in enumerate(t):
            if x not in mapping:
                mapping[x] = s[i]
            if mapping[x]!=s[i]:
                return False
        return True