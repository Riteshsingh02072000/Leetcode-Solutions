class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordSet = set(wordDict)

        def dfs(pref, suff):
            print(pref)
            print(suff)
            if suff == "":
                ans.append(" ".join(pref))
            
            for word in wordSet:
                if suff.startswith(word):
                    dfs(pref+[word], suff[len(word):])
                    # pref.append(word)
                    # suff = suff[len(word):]
                    # dfs(pref, suff)
        
        dfs([], s)
        return ans