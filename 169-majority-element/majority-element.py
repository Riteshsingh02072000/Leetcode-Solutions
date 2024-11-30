class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct= defaultdict(int)
        n = len(nums)

        for x in nums:
            dct[x] += 1
            if dct[x] > n//2:
                return x
        return -1