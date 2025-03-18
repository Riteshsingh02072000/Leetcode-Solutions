class Solution:
    def reverseString(self, nums: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1
            r-=1
        