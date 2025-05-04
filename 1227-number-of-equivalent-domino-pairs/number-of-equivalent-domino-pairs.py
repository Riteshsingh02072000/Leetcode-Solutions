class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # n = len(dominoes)

        ans = 0
        dct =defaultdict(int)
        for a, b in dominoes:
            key = min(a, b), max(a, b)
            
            ans += dct[key]
            dct[key]+=1
        return ans


        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (dominoes[i][0]==dominoes[j][1] and dominoes[i][1] == dominoes[j][0]) or (dominoes[i][0]==dominoes[j][0] and dominoes[i][1] == dominoes[j][1]):
        #             ans += 1
        # return ans