class Solution:
    def mirrorDistance(self, n: int) -> int:
        def mirror(x):
            rev = 0
            while x>0:
                rev = (rev*10) + x%10
                x//=10
            return rev
        return abs(n-mirror(n))