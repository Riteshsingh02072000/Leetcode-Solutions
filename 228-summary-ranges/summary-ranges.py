class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        l, r =0,0
        while l<len(nums):
            while r<len(nums)-1 and nums[r+1] == nums[r]+1:
                r+=1
            if r!=l:
                ans.append(f'{nums[l]}->{nums[r]}')
            else:
                ans.append(str(nums[r]))
            l = r+1
            r+=1
        return ans






