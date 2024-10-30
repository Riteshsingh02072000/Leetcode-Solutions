class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [1]*n
        dec = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    inc[i] = max(inc[i], inc[j]+1)
        

        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                if nums[j]<nums[i]:
                    dec[i] = max(dec[i], dec[j]+1)
        
        ans = 0

        for i in range(n):
            if inc[i]>1 and dec[i]>1:
                ans = max(ans, inc[i]+dec[i]-1)
        return n-ans