class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime, endTime, profit), key = lambda v:v[1])

        dp = [(0,0)]

        for s, e, p in jobs:
            index = bisect_right(dp, (s, float('inf')))

            if dp[index-1][1] + p > dp[-1][1]:
                dp.append((e, dp[index-1][1]+p))
        return dp[-1][1]