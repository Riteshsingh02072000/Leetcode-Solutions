class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        cur = root = [None]*27
        ewords = sorted(enumerate(wordsContainer), key = lambda x: len(x[1]))
        root[-1] = ewords[0][0]

        for i, word in ewords:
            cur = root
            for c in reversed(word):
                ci = ord(c) - ord('a')
                if cur[ci] is None:
                    cur[ci] = [None]*26+[i]
                cur = cur[ci]
        

        ans= []
        for word in wordsQuery:
            cur = root
            for c in reversed(word):
                ci = ord(c) - ord('a')
                if cur[ci] is None:
                    break
                cur = cur[ci]
            ans.append(cur[-1])
        return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    #     n = len(wordsQuery)
    #     ans = [-1]*n
    #     for i, q in enumerate(wordsQuery):
    #         len_ = float('inf')
    #         lcs = float('-inf')
    #         for j, word in enumerate(wordsContainer):
    #             lcs_ = self.longest_common_suffix(word, q)
    #             if lcs_>lcs:
    #                 len_ = len(word)
    #                 lcs = lcs_
    #                 ans[i] = j
    #             elif lcs_==lcs and len(word)<len_:
    #                 len_ = len(word)
    #                 ans[i] = j
                        
    #                 # ans[i] = j
    #     return ans

    # def longest_common_suffix(self, str1, str2):
    #     str1_reversed = str1[::-1]
    #     str2_reversed = str2[::-1]

    #     result = 0

    #     for i in range(min(len(str1_reversed), len(str2_reversed))):
    #         if str1_reversed[i] == str2_reversed[i]:
    #             result += 1
    #         else:
    #             break
    #     return result