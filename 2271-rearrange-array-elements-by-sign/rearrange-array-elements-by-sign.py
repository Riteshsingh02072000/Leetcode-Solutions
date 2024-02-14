class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for x in nums:
            if x<0:
                neg.append(x)
            else:
                pos.append(x)
        
        for i in range(len(nums)):
            if i%2==0:
                nums[i] = pos[i//2]
            else:
                nums[i] = neg[i//2]
        return nums