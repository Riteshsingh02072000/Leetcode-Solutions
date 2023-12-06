class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        week = n//7
        remainder = n%7
        total += 28*week
        total +=(remainder*(remainder+1))//2 + remainder*week
        total += ((week*(week-1))//2)*7

        return total