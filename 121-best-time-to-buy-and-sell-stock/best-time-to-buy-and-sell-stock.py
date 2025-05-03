class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = float('inf')
        profit = 0
        for x in prices:
            buy = min(buy, x)
            profit = max(profit,x-buy)
        return profit