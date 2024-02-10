class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = defaultdict(int)
        mag = defaultdict(int)

        for x in ransomNote:
            rans[x] +=1
         
        for x in magazine:
            mag[x] +=1
        
        for x, val in rans.items():
            if x not in mag or val>mag[x]:
                return False
        return True