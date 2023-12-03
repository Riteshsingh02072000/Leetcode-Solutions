class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ele, dig = 0,0
        for x in nums:
            ele+=x
            for i in str(x):
                dig+=int(i)
        return ele-dig