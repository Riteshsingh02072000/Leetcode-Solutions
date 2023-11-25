class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        
        index = len(piles)-2
        
        total = 0
        while n > 0:
            total += piles[index]
            index -= 2
            n -= 1
        return total