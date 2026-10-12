class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums)!=len(set(nums))
        # seen = set()
        # for x in nums:
        #     if x in seen:
        #         return True
        #     seen.add(x)
        # return False