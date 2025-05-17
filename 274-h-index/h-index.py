class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        n = len(citations)
        citations.sort()

        for i, val in enumerate(citations):
            if val<=n-i:
                ans = val
            else:
                ans = max(ans, n-i)
        return ans