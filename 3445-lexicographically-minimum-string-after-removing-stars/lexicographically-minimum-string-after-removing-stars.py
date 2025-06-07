class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        bucket = [[] for i in range(26)]
        removed =[False]*n

        for i in range(n):
            if s[i] == '*':
                removed[i] = True
                for j in range(26):
                    if bucket[j]:
                        removed[bucket[j].pop()] = True
                        break
            else:
                bucket[ord(s[i])-ord('a')].append(i)
        
        ans = []
        for i in range(n):
            if not removed[i]:
                ans.append(s[i])
        return ''.join(ans)
