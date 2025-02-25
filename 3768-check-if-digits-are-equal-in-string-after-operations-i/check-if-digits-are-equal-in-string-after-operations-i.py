class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            n = len(s)
            tmp = ""
            for i in range(n-1):
                first = int(s[i])
                second = int(s[i+1])

                pair = (first + second)%10
                tmp += str(pair)
            s = tmp
        return len(set(s)) == 1