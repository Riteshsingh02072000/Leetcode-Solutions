class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        if k ==0:
            return 1
        cnt = [0]*32
        cur = 0
        ans = float('inf')
        l = 0

        for r in range(len(nums)):
            cur|=nums[r]
            i = 0
            num = nums[r]
            while num>0:
                cnt[i] += num%2
                num//=2
                i+=1
            while cur>=k and l<=r:
                ans = min(ans, r-l+1)
                num, i = nums[l], 0
                while num>0:
                    if num%2:
                        cnt[i] -=1
                        if not cnt[i]:
                            cur ^= 1<<i
                    num//=2
                    i+=1
                l+=1
                
        return ans if ans!=float('inf') else -1