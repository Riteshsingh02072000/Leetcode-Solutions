class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        jump = 0 
        curEnd = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                jump+=1
                curEnd = farthest
        return jump
        
        # n = len(nums)
        # ans = [float('inf') for x in nums]
        # ans[0] = 0

        # for i in range(n):
        #     for j in range(nums[i]):
        #         if i+j+1<n:
        #             ans[i+j+1] = min(ans[i+j+1], 1+ans[i])
        # return ans[-1]