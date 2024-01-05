class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # idx = 0
        # for i in range(len(nums)):
        #     if i!=0 and nums[i]==nums[i-1]:
        #         continue
        #     else:
        #         nums[idx] = nums[i]
        #         idx+=1
        # return idx
        seen = set()
        i = 0
        for x in nums:
            if x not in seen:
                seen.add(x)
                nums[i] = x
                i+=1
        return i
