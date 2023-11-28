class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat, plant = 0,0
        res = 1
        
        for x in corridor:
            if x=='S':
                seat+=1
            else:
                if seat == 2:
                    plant+=1
            if seat == 3:
                res = res*(plant+1)%(10**9+7)
                seat = 1
                plant = 0
        if seat != 2:
            return 0
        return res%(10**9+7)
        