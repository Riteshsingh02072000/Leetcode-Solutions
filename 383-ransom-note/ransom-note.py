class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans = collections.defaultdict(int)
        mag = collections.defaultdict(int)

        for x in ransomNote:
            rans[x] +=1
        
        for x in magazine:
            mag[x] +=1
        
        for key, val in rans.items():
            if key not in mag or mag[key]<rans[key]:
                return False
        return True