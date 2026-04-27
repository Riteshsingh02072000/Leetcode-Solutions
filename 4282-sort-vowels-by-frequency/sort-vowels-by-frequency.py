class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = 'aeiou'
        available = ""
        for x in s:
            if x in vowels:
                available += x
        
        cnt = Counter(available)
        order = []

        for x in cnt.most_common():
            for i in range(x[1]):
                order.append(x[0])
        
        j =0 
        s = list(s)
        for i, x in enumerate(s):
            if x in vowels:
                s[i] = order[j]
                j+=1
                continue
        return ''.join(s)