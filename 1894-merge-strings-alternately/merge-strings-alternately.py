class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        i, j =0,0
        len1, len2 = len(word1), len(word2)

        while i<len1 and j<len2:
            ans += word1[i]
            ans += word2[j]
            i+=1
            j+=1
        
        while i<len1:
            ans+=word1[i]
            i+=1
        while j<len2:
            ans += word2[j]
            j+=1
        return ans