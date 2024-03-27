class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        l = 0
        ans = float('-inf')
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            if count[s[r]]>2:
                while l<r and count[s[r]]>2:
                    count[s[l]]-=1
                    l+=1
            ans = max(ans, r-l+1)
        return ans if ans!=float('-inf') else 0