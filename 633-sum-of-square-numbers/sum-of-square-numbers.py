class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))

        while left<=right:
            sum_ = left**2 + right**2
            if sum_ == c:
                return True
            elif sum_<c:
                left+=1
            else:
                right -= 1
        return False