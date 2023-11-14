class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        min_ = [float('inf')]*26
        max_ = [float('-inf')]*26

        for i in range(len(s)):
            char_index = ord(s[i]) - ord('a')
            min_[char_index] = min(min_[char_index], i)
            max_[char_index] = max(max_[char_index], i)
        
        ans = 0

        for i in range(26):
            if min_[i] == float('inf') or max_[i] == float('-inf'):
                continue
            
            unique_chars = set()
            for j in range(min_[i]+1, max_[i]):
                unique_chars.add(s[j])
            
            ans+=len(unique_chars)
        
        return ans