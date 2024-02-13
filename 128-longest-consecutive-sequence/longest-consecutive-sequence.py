class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        nums= set(nums)
        ans = 0
        for num in nums:
            if num-1 not in nums:
                cur = 1 
                while cur+num in nums:
                    cur+=1
                ans = max(ans, cur)
        return ans