class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS = defaultdict(int)
        dicT = defaultdict(int)

        for x in s:
            dicS[x] += 1
        
        for x in t:
            dicT[x] += 1
        
        return dicS == dicT