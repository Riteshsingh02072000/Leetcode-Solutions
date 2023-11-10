class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(set)

        for u,v in adjacentPairs:
            d[u].add(v)
            d[v].add(u)
        
        ans = []

        for u, ngbr in d.items():
            if len(ngbr)==1:
                ans.append(u)
                break
        
        prev = None
        n = len(adjacentPairs)+1
        cur = ans[-1]
        while len(ans)<n:
            # last = ans[-1]
            for v in d[cur]:
                if v!=prev:
                    prev = cur
                    cur = v
                    ans.append(v)
                    break
        return ans
