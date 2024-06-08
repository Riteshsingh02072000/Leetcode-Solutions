class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # n = len(nums)
        # prefix = [0]*(n+1)

        # for i in range(1, n+1):
        #     prefix[i] = prefix[i-1] + nums[i-1]
        
        # for start in range(n):
        #     for end in range(start+1, n):
        #         sum_ = prefix[end+1] - prefix[start]
        #         if sum_%k==0:
        #             return True
        # return False


        rem = {0: -1}
        remainder = 0
        for i in range(len(nums)):
            remainder += nums[i]

            if k!=0:
                remainder %= k 
            
            if remainder in rem:
                if i-rem[remainder]>=2:
                    return True
            else:
                rem[remainder] = i
        return False