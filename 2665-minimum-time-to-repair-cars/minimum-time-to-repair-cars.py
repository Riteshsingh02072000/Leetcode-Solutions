class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        
        def countcars(m):
            car = 0
            for x in ranks:
                car += int(math.sqrt(m/x))
                # car += math.floor(n)
            return car
        

        l = 1
        r = ranks[0]*(cars*cars)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            repaired = countcars(mid)
            if repaired>=cars:
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans
