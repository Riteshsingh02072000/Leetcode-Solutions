class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # def pal(x):
        #     l, r = 0, len(x)-1
        #     while l<r:
        #         if x[l]!=x[r]:
        #             return False
        #         l+=1
        #         r-=1
        #     return True

        for x in words:
            if x==x[::-1]:
                return x
        return ""