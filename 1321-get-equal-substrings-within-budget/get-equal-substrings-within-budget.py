class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
            ans = 0
            cost = 0
            l = 0

            for r in range(len(s)):
                cost += abs(ord(s[r])-ord(t[r]))

                if cost>maxCost:
                    cost -= abs(ord(s[l]) - ord(t[l]))
                    l+=1
                ans = max(ans, r-l+1)
            return ans