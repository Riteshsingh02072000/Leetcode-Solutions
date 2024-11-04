class Solution:
    def isBalanced(self, nums: str) -> bool:
        n = len(nums)
        odd = 0
        even = 0
        i = 0
        for i in range(len(nums)):
            if i %2==0:
                odd += int(nums[i])
            elif i%2==1:
                even += int(nums[i])
        
        return odd==even