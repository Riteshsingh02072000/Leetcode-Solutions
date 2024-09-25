class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        d = defaultdict(int)
        for x in words:
            s = ""
            for y in x:
                s+=y
                d[s]+=1
        
        ans = []

        for word in words:
            score = 0
            s = ""
            for x in word:
                s+=x
                score+=d[s]
            ans.append(score)
        return ans