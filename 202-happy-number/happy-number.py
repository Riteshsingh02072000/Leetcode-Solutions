class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n!=1:
            s = 0
            while n>0:
                digit = n%10
                s += digit**2
                n//=10
            if s in seen:
                return False
            n = s
            seen.add(s)

        return True