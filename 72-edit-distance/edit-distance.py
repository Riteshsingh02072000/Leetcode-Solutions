class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        @cache

        def mdistance(i, j):
            if i==n or j == m:
                return (n-i) + (m-j)
            
            operations = min(
                mdistance(i+1,j)+1,
                mdistance(i,j+1)+1,
                mdistance(i+1,j+1) + (0 if word1[i] == word2[j] else 1),
            )


            return operations
        return mdistance(0,0)