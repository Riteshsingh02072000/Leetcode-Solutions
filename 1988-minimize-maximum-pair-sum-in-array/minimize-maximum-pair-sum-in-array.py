class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = float('-inf')
        l = 0
        r = n-1

        while l<r:
            ans = max(ans, nums[l]+nums[r])
            l+=1
            r-=1
        return ans