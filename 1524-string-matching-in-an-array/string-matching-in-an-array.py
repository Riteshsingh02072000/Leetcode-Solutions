class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if i == j:
                    continue
                if x in y:
                    ans.append(x)
                    break
        return ans
                