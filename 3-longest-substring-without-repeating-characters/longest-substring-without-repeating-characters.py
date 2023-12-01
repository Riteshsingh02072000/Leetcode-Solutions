class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # if s=="":
        #     return 0
        # ans = float('-inf')
        # l = 0
        # subs = []
        # nums = list(s)
        # for r in range(len(nums)):
        #     subs += nums[r]
        #     if len(set(subs))==r-l+1:
        #         ans = max(ans, r-l+1)
        #     else:
        #         while len(set(subs))!=r-l+1:
        #             subs.pop(0)
        #             l+=1
        #         ans = max(ans, r-l+1)
        # return ans

        ans = 0
        subs = set()
        l =0
        

        for r in range(len(s)):
            while s[r] in subs:
                subs.remove(s[l])
                l+=1
            subs.add(s[r])
            ans = max(ans, len(subs))
        return ans