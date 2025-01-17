class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        n = len(nums)

        for x in nums:
            dic[x] += 1
            if dic[x] >= n/2:
                return x
        return -1