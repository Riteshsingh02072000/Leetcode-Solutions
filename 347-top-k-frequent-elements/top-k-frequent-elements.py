class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n, _ in sorted(Counter(nums).items(), key = lambda x:x[1], reverse = True)][:k]