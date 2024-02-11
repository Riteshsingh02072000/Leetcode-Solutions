class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        tmp = dict()
        if len(s)!=len(t) or len(set(s))!=len(set(t)):
            return False

        for i, v in enumerate(s):
            if v not in tmp:
                tmp[v] = t[i]
            if tmp[v] != t[i]:
                return False
        return True