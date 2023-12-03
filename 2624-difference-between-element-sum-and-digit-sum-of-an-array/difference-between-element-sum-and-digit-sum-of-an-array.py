class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele, dig = 0,0
        for x in nums:
            ele+=x
            dig += self.digit_sum(x)
        return ele-dig
    def digit_sum(self, n):
        result = 0
        while n:
            result += int(n%10)
            n //= 10
        return result
