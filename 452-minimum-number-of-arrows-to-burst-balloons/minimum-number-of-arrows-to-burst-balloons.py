class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        cur_end = float('-inf')
        ans = 0
        for start, end in points:
            if start>cur_end:
                ans+=1
                cur_end = end


        # print(points)
        return ans