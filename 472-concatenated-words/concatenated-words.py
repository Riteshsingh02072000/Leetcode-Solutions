class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        words = set(words)
        @lru_cache(None)
        def dfs(word):
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in words and suffix in words:
                    return True
                if prefix in words and dfs(suffix):
                    return True
            return False
        
        ans = []
        for word in words:
            if dfs(word):
                ans.append(word)
        return ans