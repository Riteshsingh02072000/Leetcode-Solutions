class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        prev = points[0][:]

        for i in range(1, m):
            l_max = [0] * n 
            r_max = [0] * n

            l_max[0] = prev[0]
            for j in range(1, n):
                l_max[j] = max(l_max[j-1] - 1, prev[j])

            r_max[-1] = prev[-1]
            for j in range(n-2, -1, -1):
                r_max[j] = max(r_max[j+1] - 1, prev[j])

            for j in range(n):
                prev[j] = points[i][j] + max(l_max[j], r_max[j])

        return max(prev)
