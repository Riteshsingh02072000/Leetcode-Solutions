class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = len(set(nums))
        if not(nums[0]+nums[1]>nums[2] and nums[0]+nums[2]>nums[1] and nums[1]+nums[2]>nums[0]):
            return "none"
        if n ==1:
            return "equilateral"
        elif n==2:
            return "isosceles"
        else:
            return "scalene"