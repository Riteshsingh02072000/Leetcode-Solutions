class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        
        for x in range(k+1):
            ans += min(tickets[x], tickets[k])
        
        for y in range(k+1, len(tickets)):
            ans += min(tickets[y], tickets[k] -1)
            
        return ans