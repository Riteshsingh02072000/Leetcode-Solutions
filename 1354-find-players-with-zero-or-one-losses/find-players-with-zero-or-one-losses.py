class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        outgoing = collections.defaultdict(int)
        seen = set()
        for x, y in matches:
            outgoing[y] +=1
            seen.add(x)
            seen.add(y)
        print(seen)
        ans = [[], []]
        
        for x in list(seen):
            if x not in outgoing:
                ans[0].append(x)
            else:
                if outgoing[x]==1:
                    ans[1].append(x)

        ans[0].sort()
        ans[1].sort()
        return ans
        # for key, val in outgoing.values():
        #     if