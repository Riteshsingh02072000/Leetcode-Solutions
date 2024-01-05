class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = collections.defaultdict(int)
        for x in nums:
            dct[x]+=1
            if dct[x] >= len(nums)/2:
                return x
