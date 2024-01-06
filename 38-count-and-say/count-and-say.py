class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        ans = '1'

        for i in range(n-1):
            l, r = 0, 0
            curS = ""

            while l<len(ans):
                c = 0
                while r<len(ans) and ans[l] == ans[r]:
                    c+=1
                    r+=1
                curS += str(c)
                curS += str(ans[l])
                l = r
            ans = curS
        return ans 