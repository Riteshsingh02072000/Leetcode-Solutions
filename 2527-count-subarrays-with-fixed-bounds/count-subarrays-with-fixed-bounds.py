class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        bad_idx, left_idx, right_idx = -1, -1, -1
        ans = 0

        for i, num in enumerate(nums):
            if not minK<=num<=maxK:
                bad_idx = i
            
            if num == minK:
                left_idx = i
            
            if num == maxK:
                right_idx = i
            
            ans += max(0, min(left_idx, right_idx)-bad_idx)
        return ans