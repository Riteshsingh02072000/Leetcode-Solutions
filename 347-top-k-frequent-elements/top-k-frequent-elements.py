class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = collections.Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for key, v in cnt.items():
            bucket[v].append(key)
        
        ans = []
        for i in range(len(bucket)-1, 0, -1):
            for num in bucket[i]:
                ans.append(num)

                if len(ans) == k:
                    return ans
        return ans


        # return [n for n, _ in sorted(Counter(nums).items(), key = lambda x:x[1], reverse = True)][:k]



