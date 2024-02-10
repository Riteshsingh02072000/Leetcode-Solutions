class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat = dict()
        s = s.split()
        print(s)
        if len(pattern) != len(s) or len(set(pattern))!=len(set(s)):
            return False

        for i in range(len(s)):
            if s[i] not in pat:
                pat[s[i]] = pattern[i]
            elif pat[s[i]] != pattern[i]:
                return False
        return True