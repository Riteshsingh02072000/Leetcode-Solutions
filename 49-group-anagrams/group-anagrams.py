class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        
        for x in strs:
            word = list(x)
            word.sort()
            print(word)
            cur = ''.join(word)
            anag[cur].append(x)
        ans = []
        for x in anag.values():
            ans.append(x)
        return ans
