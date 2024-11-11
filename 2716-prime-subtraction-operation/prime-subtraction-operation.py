class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        if nums == sorted(nums) and len(set(nums)) == len(nums):
            return True
        
        def sieve(limit):
            prime = [True]*(limit+1)
            prime[0], prime[1] = False, False
            for num in range(2, int(limit**0.5)+1):
                if prime[num]:
                    for j in range(num*num, limit+1, num):
                        prime[j] = False
            ans = [num for num in range(2, limit+1) if prime[num]]
            return ans
        
        arr = sieve(1000)
        for i in range(len(nums)):
            if i ==0:
                ind = bisect.bisect_left(arr, nums[i])
                if ind == 0:
                    continue
                nums[i] -= arr[ind-1]
            else:
                if nums[i] <= nums[i-1]:
                    return False
                val = nums[i] - nums[i-1]
                ind = bisect.bisect_left(arr, val)
                if ind == 0:
                    continue
                nums[i] -= arr[ind-1]
        return nums == sorted(nums)
