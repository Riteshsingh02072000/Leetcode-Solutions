class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        ans.append(s[:spaces[0]])

        for i in range(1, len(spaces)):
            ans.append(s[spaces[i-1]: spaces[i]])
        ans.append(s[spaces[-1]:])
        return ' '.join(ans)