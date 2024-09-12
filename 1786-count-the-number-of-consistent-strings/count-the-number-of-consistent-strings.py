class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)

        ans = 0 
        for x in words:
            if all(char in allowed for char in x):
                ans+=1
        return ans