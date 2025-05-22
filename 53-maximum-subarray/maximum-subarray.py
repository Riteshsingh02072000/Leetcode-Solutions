class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        cur = 0
        # if len(nums) == 1:
        #     return nums[0]

        for x in nums:
            cur += x
            ans = max(ans, cur)
            if cur<0:
                cur = 0
                continue
            
        return ans