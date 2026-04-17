class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def mirror(x):
            rev = 0
            while x:
                rev = (rev*10) + (x%10)
                x//=10
            return rev

        mp = {}
        ans = float('inf')
        for i, num in enumerate(nums):
            if num in mp:
                ans = min(ans, i - mp[num])
            mp[mirror(num)] = i
        return -1 if ans==float('inf') else ans