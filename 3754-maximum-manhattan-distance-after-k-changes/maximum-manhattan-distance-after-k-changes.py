class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
    
        for ns in ['N', 'S']:
            for ew in ['E', 'W']:
                i = 0
                allowed_k = k
                curManhattan = 0
                for j in range(n):
                    if s[j] not in (ns, ew):
                        if allowed_k > 0:
                            allowed_k-=1
                            curManhattan += 1
                        else:
                            # do some removals
                            while i < j and s[i] in (ns, ew):
                                i+=1
                            i+=1
                            curManhattan-=1
                    else:
                        curManhattan += 1
                    
                    ans = max(ans, curManhattan)
        return ans
