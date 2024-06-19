class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m*k>len(bloomDay):
            return -1
        
        l, r = min(bloomDay), max(bloomDay)
        ans = r


        while l<=r:
            mid = (l+r)//2
            count, bouquets, adjacent = 0, 0, False

            for x in bloomDay:
                if x<=mid:
                    if not count:
                        adjacent = True
                        count+=1
                    elif adjacent:
                        count+=1
                else:
                    count = 0
                    adjacent = False
                
                if count == k:
                    bouquets+=1
                    adjacent = False
                    count = 0
            if bouquets>=m:
                ans = min(ans, mid)
                r = mid -1
            else:
                l = mid+1
        return ans