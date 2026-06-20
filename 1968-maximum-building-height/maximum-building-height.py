class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        if not restrictions:
            return n-1
        
        restrictions.sort()

        num, h = 1, 0

        for i in range(len(restrictions)):
            x, y = restrictions[i]
            restrictions[i][1] = min(y, x-num+h)
            num, h = x, restrictions[i][1]
        
        for i in range(len(restrictions)-2, -1, -1):
            restrictions[i][1] = min(restrictions[i][1], restrictions[i+1][1]+restrictions[i+1][0]-restrictions[i][0])
        
        ans = n-restrictions[-1][0]+restrictions[-1][1]
        num, h = 1, 0

        for x, y in restrictions:
            steps = x-num-abs(y-h)
            higher = max(y, h)
            ans = max(ans, higher + steps//2)
            num, h = x, y
        return ans
        