class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        curMax, curMin = 1,1

        for x in nums:
            tmp = max(x, x*curMin, x*curMax)
            curMin = min(x, x*curMin, x*curMax)

            curMax = tmp
            ans = max(ans, curMax)
        return ans