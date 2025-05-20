class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        ans = [0]*n

        for l, r in queries:
            ans[l] += 1
            if r+1<n:
                ans[r+1] -= 1
        prefix = 0
        for i in range(n):
            prefix+=ans[i]
            ans[i] = prefix
        # print(ans)

        
        for i, x in enumerate(nums):
            if nums[i]>ans[i]:
                return False
        return True