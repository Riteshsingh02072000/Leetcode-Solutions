class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def mirror(x):
            return int(str(x)[::-1])

        mp = defaultdict(int)
        ans = float('inf')
        for i, num in enumerate(nums):
            if num in mp:
                ans = min(ans, abs(mp[num]-i))
            mp[mirror(num)] = i

        
        return -1 if ans==float('inf') else ans