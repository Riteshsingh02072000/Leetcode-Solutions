class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = dict()

        for i, x in enumerate(nums):
            if target-x in mapping:
                return [mapping[target-x], i]
            mapping[x] = i