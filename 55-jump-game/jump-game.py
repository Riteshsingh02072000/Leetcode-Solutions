class Solution:
    def canJump(self, nums: List[int]) -> bool:
        top = nums[0]

        for i in range(1, len(nums)):
            if top<i:
                return False
            top = max(top, i+nums[i])
        return True
