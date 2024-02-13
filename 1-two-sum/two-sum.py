class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = defaultdict(int)
        for i, x in enumerate(nums):
            if target-x in check :
                return [check[target-x], i]
            else:
                check[x] = i
        return []