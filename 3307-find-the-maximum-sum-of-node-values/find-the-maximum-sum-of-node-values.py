class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        ans = 0
        changes = 0
        min_sacrifice = float('inf')

        for val in nums:
            tmp = val^k
            if tmp>val:
                changes += 1
                ans += tmp
                min_sacrifice = min(min_sacrifice, tmp-val)
            else:
                ans += val
                min_sacrifice = min(min_sacrifice, val- tmp)
        if changes%2:
            ans -= min_sacrifice
        return ans