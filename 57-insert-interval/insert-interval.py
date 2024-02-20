class Solution:
    def insert(self, x: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        x.append(newInterval)
        x.sort()
        ans = [x[0]]
        for i in range(1, len(x)):
            if x[i][0] <=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], x[i][1])
            else:
                ans.append(x[i])
        return ans