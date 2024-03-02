class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # nums.sort(key = lambda x:abs(x))
        # ans = [x**2 for x in nums]
        # return ans

        ans = [0]*len(nums)
        l, r, i = 0, len(nums)-1, len(nums)-1

        while l<=r:
            val = 0
            if nums[l]**2 >= nums[r]**2:
                val = nums[l]**2
                l+=1
            else:
                val = nums[r]**2
                r-=1
            ans[i] = val
            i-=1
        return ans