class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)

        for x in strs:
            word = list(x)
            word.sort()
            word = ''.join(word)
            anag[word].append(x)
        
        ans = []
        for val in anag.values():
            ans.append(val)
        return ans