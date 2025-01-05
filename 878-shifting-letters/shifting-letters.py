class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        prefix = [sum(shifts)]
        for i in range(len(shifts)-1):
            prefix.append(prefix[-1]-shifts[i])
        # print(prefix)
        for i in range(len(s)):
            cur = ord(s[i]) - ord('a')
            print(cur)
            cur= (cur+prefix[i])%26
            # print(chr(cur))
            shifts[i] = chr(97+cur)
            

        return ''.join(shifts)