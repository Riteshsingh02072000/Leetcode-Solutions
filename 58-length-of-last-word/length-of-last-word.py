class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = [x for x in s.split() if x!= " "]
        return len(s[-1])