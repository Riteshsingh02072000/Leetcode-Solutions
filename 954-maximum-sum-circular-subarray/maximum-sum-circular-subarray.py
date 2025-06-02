class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if max(nums)<0:
            return max(nums)
        
        maxSum = curMax = minSum = curMin = nums[0]

        for i in range(1, len(nums)):
            curMax = max(curMax+nums[i], nums[i])
            maxSum = max(maxSum, curMax)
            curMin = min(curMin + nums[i], nums[i])
            minSum = min(minSum, curMin)
        return max(maxSum, sum(nums)-minSum)
        