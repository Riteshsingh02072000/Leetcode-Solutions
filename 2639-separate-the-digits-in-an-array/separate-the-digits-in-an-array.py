class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans =[]
        for n in nums:
            i=0
            n = str(n)
            while i<len(n):
                ans.append(int(n[i]))
                i+=1
        return ans