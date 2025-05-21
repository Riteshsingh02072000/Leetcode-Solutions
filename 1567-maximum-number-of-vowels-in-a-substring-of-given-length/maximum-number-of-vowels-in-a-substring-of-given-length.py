class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = 'aeiou'
        count = 0
        l = 0
        ans = float('-inf')

        for i in range(k):
            if s[i] in vowel:
                count += 1
        ans = max(ans, count)

        for i in range(k, len(s)):
            count -= 1 if s[l] in vowel else 0
            l+=1
            count += 1 if s[i] in vowel else 0
            ans = max(ans, count)
        return ans