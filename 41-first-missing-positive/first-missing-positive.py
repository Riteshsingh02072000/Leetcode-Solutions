class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0

        while i<n:
            cur_pos = nums[i] - 1
            if nums[i] > n or nums[i]<=0:
                i+=1
                continue
            if cur_pos!=i and cur_pos < n and nums[cur_pos] != nums[i]:
                nums[i], nums[cur_pos] = nums[cur_pos], nums[i]
            else:
                i+=1

        for i in range(1, n+1):
            if i != nums[i-1]:
                return i
        return n+1