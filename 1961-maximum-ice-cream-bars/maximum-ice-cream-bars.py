class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0 
        costs.sort()
        for x in costs:
            if coins<x:
                return ans
            coins -= x
            ans += 1
        return ans