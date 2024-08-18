class Solution:
    def nthUglyNumber(self, n: int) -> int:
        i2, i3, i5 = 0, 0, 0
        ans = [1]

        while n>1:
            u2, u3, u5 = 2*ans[i2], 3*ans[i3], 5*ans[i5]
            umin = min(u2, u3, u5)

            if umin == u2:
                i2+=1
            if umin == u3:
                i3+=1
            if umin == u5:
                i5+=1
            
            ans.append(umin)
            n-=1
        return ans[-1]
