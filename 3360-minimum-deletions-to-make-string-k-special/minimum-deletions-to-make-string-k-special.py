class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = defaultdict(int)
        for x in word:
            freq[x] += 1            
        
        freqs = sorted(freq.values(), reverse = True)
        ans = float('inf')
        for i in range(len(freqs)):
            trgt = freqs[i] 
            d = 0
            for f in freqs:
                if f>trgt+k:
                    d+= f-(trgt+k)
                elif f<trgt:
                    d+=f
            ans = min(ans, d)
            if ans == 0:
                break
        return ans if ans!=float('inf') else 0