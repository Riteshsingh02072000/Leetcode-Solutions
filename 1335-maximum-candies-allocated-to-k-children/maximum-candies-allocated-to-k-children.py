class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if k>sum(candies):
            return 0
        ans = 0
        l,r = 1, max(candies)

        while l<=r:
            mid = (l+r)//2
            sum_ = 0
            for i in range(len(candies)):
                sum_ += candies[i]//mid
            
            if sum_>=k:
                ans = max(ans, mid)
                l = mid+1
            else:
                r = mid-1
        
        return ans