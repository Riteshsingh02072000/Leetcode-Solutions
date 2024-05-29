class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0 
        x = (int(s, 2))
        print(x)
        

        while x!=1:
            if x%2==0:
                x//=2
            else:
                x+=1
            ans += 1
        return ans