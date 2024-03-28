class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l =0
        ans = float('-inf')
        window = defaultdict(int)

        for r in range(len(nums)):
            window[nums[r]] += 1
            if window[nums[r]] > k:
                while l<r and window[nums[r]]>k:
                    window[nums[l]] -= 1
                    l+=1
            ans = max(ans, r-l+1)
        return ans