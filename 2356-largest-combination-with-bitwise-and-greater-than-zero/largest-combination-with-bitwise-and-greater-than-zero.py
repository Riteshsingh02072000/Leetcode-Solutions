class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bits = [0]*32
        for num in candidates:
            j = 0
            while num>0:
                bits[j] += (num&1)
                num>>=1
                j+=1
        return max(bits)