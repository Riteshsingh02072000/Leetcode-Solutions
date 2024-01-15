class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outgoing = collections.defaultdict(int)
        # seen = set()
        for x, y in matches:
            outgoing[x] += 0
            outgoing[y] += 1
            # seen.add(x)
            # seen.add(y)
        # print(seen)
        # ans = [[], []]
        
        zero = sorted([x for x, v in outgoing.items() if v==0])
        ones = sorted([x for x, v in outgoing.items() if v==1])

        # ans[0].sort()
        # ans[1].sort()
        return [zero, ones]
        # for key, val in outgoing.values():
        #     if