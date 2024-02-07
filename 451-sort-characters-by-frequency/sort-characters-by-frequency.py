class Solution:
    def frequencySort(self, s: str) -> str:
        res=''
        ans = collections.Counter(list(s))
        ans = sorted(ans.items(), key = lambda x:x[1], reverse = True)
        for i, v in ans:
            res += i*v
        return res