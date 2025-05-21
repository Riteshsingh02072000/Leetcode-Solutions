class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        # if len(ranks) == 1:
        #     return ranks[0]*(cars**2)

        def countCar(m):
            ans = 0
            for x in ranks:
                ans += int(math.sqrt(m/x))
            return ans
        
        l, r = 1, ranks[0]*(cars**2)
        ans = 0
        while l<=r:
            mid = (l+r)//2
            repaired = countCar(mid)
            if repaired >= cars:
                ans = mid
                r = mid -1
            else:
                l = mid+1
        return ans

