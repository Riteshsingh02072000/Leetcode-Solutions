class Solution:
    def canJump(self, nums: List[int]) -> bool:
        top = nums[0]
        for i in range(1, len(nums)):
            if i>top :
                return False
            top = max(top, i + nums[i])
            if top>=len(nums)-1:
                return True
        return True