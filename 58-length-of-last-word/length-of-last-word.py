class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # s = [x for x in s.split() if x!=" "]
        # # s = [x for x in s.split() if x!= " "]
        # return len(s[-1])
        return len(s.strip().split()[-1])