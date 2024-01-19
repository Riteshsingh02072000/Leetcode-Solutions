class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        print(zip(strs))
        ans = ""
        for x in zip(*strs):
            if len(set(x))==1:
                ans+= str(x[0])
            else:
                return ans
        return ans