class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        l=0
        count = defaultdict(int)
        for r in range(n):
            count[s[r]]+=1
            while count[s[r]]>1:
                count[s[l]] -= 1
                l+=1
            ans = max(ans, r-l+1)
        return ans
