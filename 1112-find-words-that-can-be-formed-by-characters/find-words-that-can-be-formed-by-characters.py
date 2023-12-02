class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        freq = collections.defaultdict(int)

        for x in chars:
            freq[x] +=1
        
        for i in words:
            for j in i:
                if freq[j] < i.count(j):
                    break
            else:
                ans+=len(i)
        return ans