class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dct = collections.defaultdict(int)
        i = 0
        for x in nums:
            dct[x] +=1
            if dct[x]>2:
                continue
            else:
                nums[i] = x
                i+=1
        return i