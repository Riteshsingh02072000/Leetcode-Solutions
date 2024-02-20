class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # i = 0
        # while i<len(nums):
        #     if i not in nums:
        #         return i
        #     i+=1
        # return len(nums)

        return sum(list(range(len(nums)+1))) - sum(nums)