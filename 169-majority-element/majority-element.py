class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dct = defaultdict(int)
        for x in nums:
            dct[x] += 1
            if dct[x]>=n/2:
                return x
        