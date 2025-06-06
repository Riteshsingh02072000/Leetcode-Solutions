class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        last_pos = {}
        res = [0]*n
        kCount = [0]*(n+1)
        

        for i, ele in enumerate(nums):
            kCount[i+1] = kCount[i] + int(ele == k)
            res[i] = kCount[i] + 1
            if ele in last_pos:
                res[i] = max(res[i], res[last_pos[ele]] + 1)
            last_pos[ele] = i
        
        for i in range(n):
            res[i] += (kCount[-1]-kCount[i+1])
        return max(res)