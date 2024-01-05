class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # dct = collections.defaultdict(int)
        # for x in nums:
        #     dct[x]+=1
        #     if dct[x] >= len(nums)/2:
        #         return x

        count = 0 
        ans = 0

        for x in nums:
            if count == 0:
                ans = x
            
            if x == ans:
                count+=1
            
            else:
                count -=1
        return ans