class Solution:
    def getLucky(self, s: str, k: int) -> int:
        digit = ''
        for x in s:
            digit+=str(ord(x)-ord('a')+1)
        print(digit)
        for i in range(k):
            ans = 0

            for x in digit:
                ans+= int(x)
            digit = str(ans)

        return int(digit)
