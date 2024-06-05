class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        ans = []
        for i in range(26):
            char = chr(ord('a') + i)
            min_count = float('inf')

            for word in words:
                min_count = min(min_count, word.count(char))
                if min_count == 0:
                    break
                
            ans.extend([char]*min_count)
        return ans
