class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        @cache

        def helper(i, j):
            if i == n1 or j == n2:
                return (n1-i) + (n2-j)
            
            operations = min(
                helper(i+1, j)+1, #delete
                helper(i, j+1)+1, #insert
                helper(i+1, j+1) + (0 if word1[i]==word2[j] else 1) #replace
            )
            return operations
        
        return helper(0, 0)
