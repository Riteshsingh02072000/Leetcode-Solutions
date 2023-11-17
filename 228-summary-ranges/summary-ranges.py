class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        ans = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    ans.append(str(start))
                else:
                    ans.append(str(start) + '->' + str(nums[i-1]))
                start = nums[i]
        
        if start == nums[-1]:
            ans.append(str(start))
        else:
            ans.append(str(start) + '->' + str(nums[-1]))
        
        return ans