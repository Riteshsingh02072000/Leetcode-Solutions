class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums)<3:
            return 0 
        ans = 0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j, len(nums)-1
                while l<r:
                    mid = (l+r+1)//2
                    if nums[mid] < (nums[i]+nums[j]):
                        l = mid
                    else:
                        r=mid-1
                ans+= (l-j)
        return ans