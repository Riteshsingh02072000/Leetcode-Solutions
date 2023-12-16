class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len((t)):
            return False
        freq_s = collections.defaultdict(int)
        freq_t = collections.defaultdict(int)

        for x in s:
            freq_s[x] +=1
        
        for y in t:
            freq_t[y] +=1
        

        return freq_s == freq_t