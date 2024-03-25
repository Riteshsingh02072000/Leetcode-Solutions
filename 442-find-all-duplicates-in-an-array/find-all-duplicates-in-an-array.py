class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dct = defaultdict(int)
        ans = []
        for x in nums:
            dct[x] += 1
            if dct[x] == 2:
                ans.append(x)
        return ans