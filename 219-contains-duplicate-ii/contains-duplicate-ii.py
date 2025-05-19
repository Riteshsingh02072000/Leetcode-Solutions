class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(int)

        for i, x in enumerate(nums):
            if x in dic and abs(dic[x]-i)<=k:
                return True
            dic[x] = i
        return False