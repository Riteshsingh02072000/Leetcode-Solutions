class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        # mx,ans,l,r,n=max(nums),0,0,0,len(nums)
        # while r<n:
        #     k-= nums[r]==mx
        #     r+=1
        #     while k==0:
        #         k+=nums[l]==mx
        #         l+=1
        #     ans+=l
        # return ans

        mx = max(nums)
        l = 0
        ans = 0

        for r in range(len(nums)):
            k -= nums[r]==mx
            while k==0:
                k+=nums[l]==mx
                l+=1
            ans += l
        return ans