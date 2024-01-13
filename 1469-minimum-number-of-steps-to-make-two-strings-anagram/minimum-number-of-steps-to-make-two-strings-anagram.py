class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # dicts = collections.defaultdict(int)
        # dictt = collections.defaultdict(int)
        # ans = 0
        
        # for x in s:
        #     dicts[x]+=1
        
        # for y in t:
        #     dictt[y] +=1
        
        # for key, val in dicts.items():
        #     if dicts[key]>dictt[key]:
        #         ans+= (val-dictt[key])
        # return ans

        count = [0]*26
        ans = 0
        for i in range(len(s)):
            count[ord(t[i]) - ord('a')] +=1
            count[ord(s[i]) - ord('a')] -=1
        
        for i in range(26):
            ans += max(0, count[i])
        return ans



