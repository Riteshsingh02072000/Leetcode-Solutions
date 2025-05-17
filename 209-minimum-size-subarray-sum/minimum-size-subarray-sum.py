class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        ans = float('inf')
        n = len(nums)
        total = 0

        for r in range(n):
            total += nums[r]
            while total>=target:
                ans = min(ans, r-l+1)
                total -= nums[l]
                l += 1
        return ans if ans!=float('inf') else 0