class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = float('-inf')
        cur = 0
        for x in s:
            if x=='E':
                cur+=1

            elif x=='L':
                cur-=1
            
            ans = max(ans, cur)
        return ans