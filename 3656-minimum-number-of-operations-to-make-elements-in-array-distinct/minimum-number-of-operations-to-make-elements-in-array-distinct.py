class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while len(set(nums))!=len(nums):
            n = len(nums)
            nums = nums[min(3, n):]
            count += 1
        return count