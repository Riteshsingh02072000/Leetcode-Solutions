class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        ans = float('inf')
        l = 0
        add = 0

        for r in range(len(nums)):
            add+=nums[r]
            while add>=target:
                ans = min(ans, r-l+1)
                add-=nums[l]
                l+=1
        return ans if ans!=float('inf') else 0