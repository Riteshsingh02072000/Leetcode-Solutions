class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        max_stop = max(max(route) for route in routes)
        if max_stop<target:
            return -1
        
        n = len(routes)
        dp = [float('inf')]*(max_stop+1)
        dp[source] = 0

        flag = True

        while flag:
            flag = False
            for route in routes:
                mini = float('inf')
                for stop in route:
                    mini = min(mini, dp[stop])
                mini+=1

                for stop in route:
                    if dp[stop]>mini:
                        dp[stop] = mini
                        flag = True
        return dp[target] if dp[target]<float('inf') else -1