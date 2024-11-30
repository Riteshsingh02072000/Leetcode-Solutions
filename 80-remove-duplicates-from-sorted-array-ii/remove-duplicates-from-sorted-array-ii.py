class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = defaultdict(int)
        i = 0
        for x in nums:
            dct[x] += 1
            if dct[x] >=3:
                continue
            nums[i] = x
            i+=1
        return i