class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # vowels = "aeiouAEIOU"
        # c1, c2 = 0, 0
        # n = len(s)
        # for i in range(n):
        #     if s[i] in vowels: 
        #         if i<n//2:
        #             c1+=1
        #         else:
        #             c2+=1
        # return c1==c2


        memo = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        left, right = 0, 0

        hal_l = len(s) // 2

        for l, r in zip(s[:hal_l], s[hal_l:]):
            if l in memo: left += 1
            if r in memo: right += 1

        return left == right
        