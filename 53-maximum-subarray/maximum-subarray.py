class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = nums[0]
        # if len(nums) == 1:
        #     return nums[0]

        for i in range(1, len(nums)):
            cur = max(cur+nums[i], nums[i])
            ans = max(ans, cur)
        return ans
        # for x in nums:
        #     cur += x
        #     ans = max(ans, cur)
        #     if cur<0:
        #         cur = 0
        #         continue
            
        # return ans