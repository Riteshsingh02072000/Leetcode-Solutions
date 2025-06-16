class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = -1
        n = len(nums)
        for i in range(n-1):
            for j in range(i+1, n):
                if nums[i]>=nums[j]:
                    continue
                else:
                    ans = max(ans, (nums[j]-nums[i]))
        return ans