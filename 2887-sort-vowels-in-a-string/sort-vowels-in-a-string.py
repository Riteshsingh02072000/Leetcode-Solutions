class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        present = []
        s = list(s)
        for x in s:
            if x in vowels:
                present.append(x)
        present.sort()
        tmp = 0
        for i,x in enumerate(s):
            if x in vowels:
                s[i] = present[tmp]
                tmp += 1
        return ''.join(s)

                
        