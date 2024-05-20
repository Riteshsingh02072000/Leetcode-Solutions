class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.checkXor(nums, 0, 0)
    
    def checkXor(self, nums, index, cur):
        if index == len(nums):
            return cur

        include = self.checkXor(nums, index+1, cur^nums[index])
        exclude = self.checkXor(nums, index+1, cur)

        return include+exclude