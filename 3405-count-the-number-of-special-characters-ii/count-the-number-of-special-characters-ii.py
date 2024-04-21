class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # ans = 0
        # special_letters = set()

        # for c in word:
        #     if c.islower() and c.upper() in word:
        #         special_letters.add(c)

         
        # for letter in special_letters:
        #     if word.index(letter.upper()) > word.rindex(letter):
        #         ans += 1

        # return ans
        word_set = set(word)
        dct = {}
        ans = 0
        for i, c in enumerate(word):
            if 0<=ord(c)-ord('A')<26:
                if c not in dct:
                    dct[c] = i
            else:
                dct[c] = max(dct.get(c, 0), i)
        
        for i in range(26):
            a = chr(ord('a')+i)
            b = chr(ord('A')+i)

            if a in word_set and b in word_set and dct[b]>dct[a]:
                ans+=1
        return ans
