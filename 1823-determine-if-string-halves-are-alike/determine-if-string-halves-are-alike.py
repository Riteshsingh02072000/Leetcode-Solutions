class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        
        count = 0
        n = len(s)
        for i in range(n//2):
            if s[i] in "aeiouAEIOU":
                count+=1
        for i in range(n//2,n):
            if s[i] in "aeiouAEIOU":
                count-=1
        return count==0


        # memo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        # left, right = 0, 0

        # hal_l = len(s) // 2

        # for l, r in zip(s[:hal_l], s[hal_l:]):
        #     if l in memo: left += 1
        #     if r in memo: right += 1

        # return left == right
        