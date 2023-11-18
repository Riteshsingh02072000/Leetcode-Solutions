class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        for r in range(len(nums)):
            k += nums[r]

            if k<(r-l+1) * nums[r]:
                k-=nums[l]
                l+=1
        return r-l+1