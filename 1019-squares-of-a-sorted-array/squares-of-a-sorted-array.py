class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        nums.sort(key = lambda x:abs(x))
        ans = [x**2 for x in nums]
        return ans