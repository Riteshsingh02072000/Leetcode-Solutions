class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        # n = len(dominoes)

        ans = 0
        dct =defaultdict(int)
        for x in dominoes:
            x.sort()
            x = ''.join([str(i) for i in x])
            if x in dct:
                ans += dct[x]
            dct[x]+=1
        return ans


        # ans = 0
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if (dominoes[i][0]==dominoes[j][1] and dominoes[i][1] == dominoes[j][0]) or (dominoes[i][0]==dominoes[j][0] and dominoes[i][1] == dominoes[j][1]):
        #             ans += 1
        # return ans