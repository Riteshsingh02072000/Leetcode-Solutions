class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        present = []
        index = []
        s = list(s)
        for i,x in enumerate(s):
            if x in vowels:
                present.append(x)
                index.append(i)
        present.sort()
        tmp = 0
        for val, idx in zip(present, index):
            s[idx] = val
        return ''.join(s)
                
        