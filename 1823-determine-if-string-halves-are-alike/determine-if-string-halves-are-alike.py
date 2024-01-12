class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        c1, c2 = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] in vowels: 
                if i<n//2:
                    c1+=1
                else:
                    c2+=1
        return c1==c2
            
        