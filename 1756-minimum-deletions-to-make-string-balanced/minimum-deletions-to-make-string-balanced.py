class Solution:
    def minimumDeletions(self, s: str) -> int:
        count = 0 
        ans = 0
        for x in s:
            if x == 'b':
                count+=1
            elif count:
                ans+=1
                count-=1
        return ans