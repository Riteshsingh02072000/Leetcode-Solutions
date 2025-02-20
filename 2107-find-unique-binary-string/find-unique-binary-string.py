class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        numSet = set(nums)

        def backtrack(binary):
            if len(binary) == n:
                if binary not in numSet:
                    return binary
                return None
            
            res = backtrack(binary+'0')
            if res: return res
            return backtrack(binary + '1')
        return backtrack("")