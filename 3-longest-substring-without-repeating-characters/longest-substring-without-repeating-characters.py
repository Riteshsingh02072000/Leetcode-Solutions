class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        ans = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] += 1
            while count[s[r]]>1:
                count[s[l]] -= 1
                l+=1
            ans = max(ans, r-l+1)
        return ans