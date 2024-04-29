class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0 
        for n in nums:
            xor = xor^n
        
        ans = 0

        while k or xor:
            if (k%2) != (xor%2):
                ans+=1
            k//=2
            xor//=2
        return ans 