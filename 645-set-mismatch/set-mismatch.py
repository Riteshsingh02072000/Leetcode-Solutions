class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = [-1, -1]
        for i in range(1, len(nums)+1):
            count = nums.count(i)
            if count==2:
                ans[0] = i
            elif count == 0:
                ans[1] = i
        return ans