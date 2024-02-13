class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag = defaultdict(list)
        ans = []

        for word in strs:
            word_list = list(word)
            word_list.sort()

            cur = ''.join(word_list)
            anag[cur].append(word)
        
        for val in anag.values():
            ans.append(val)

        return ans
