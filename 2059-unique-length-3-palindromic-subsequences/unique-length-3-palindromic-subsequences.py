class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        l = set()
        r = Counter(s)

        for m in s:
            r[m] -= 1
            for c in l:
                if r[c]>0:
                    res.add((m, c))
            l.add(m)
        return len(res)

        # unique = set(s)
        # ans = 0

        # for x in unique:
        #     start = s.find(x)
        #     end = s.rfind(x)

        #     if start<end:
        #         ans += len(set(s[start+1: end]))
        # return ans