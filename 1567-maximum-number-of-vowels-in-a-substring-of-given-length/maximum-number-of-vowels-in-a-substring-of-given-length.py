class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        ans = float('-inf')
        l = 0
        vowels = 'aeiou'

        for i in range(k):
            if s[i] in vowels:
                count += 1
        ans = max(ans, count)
        if ans == k:
            return k
        
        for i in range(k, len(s)):
            count -= 1 if s[l] in vowels else 0
            l += 1
            count += 1 if s[i] in vowels else 0
            ans = max(ans, count)
        return ans

