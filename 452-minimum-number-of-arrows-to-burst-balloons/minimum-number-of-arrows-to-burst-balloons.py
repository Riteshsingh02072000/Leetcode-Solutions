class Solution:
    def findMinArrowShots(self, x: List[List[int]]) -> int:
        
        x = sorted(x, key = lambda x:x[1])
        ans= 0
        cur = float('-inf')

        for start, end in x:
            if start>cur:
                ans+=1
                cur = end

        return ans