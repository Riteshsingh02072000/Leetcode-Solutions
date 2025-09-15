class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        ans = []
        for x in sorted(nums, reverse =True):
            if x not in ans:
                ans.append(x)
                if len(ans) == k:
                    return ans
        return ans