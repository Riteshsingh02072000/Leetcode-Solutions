class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 0
        tmp = []
        for i in range(len(nums)):
            if i == 0 or nums[i]>tmp[-1]:
                ans+=1
                tmp.append(nums[i])
            else:
                x = bisect_left(tmp, nums[i])
                tmp[x] = nums[i]
        return ans
        