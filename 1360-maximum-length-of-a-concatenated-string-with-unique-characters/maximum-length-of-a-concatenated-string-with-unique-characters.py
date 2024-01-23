class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def unique(arr):
            return len(set(arr)) == len(arr)
        
        def backtrack(start, subarr):
            nonlocal ans
            if unique(subarr):
                ans = max(ans, len(subarr))
            
            for i in range(start, len(arr)):
                backtrack(i+1, subarr+arr[i])
            
        ans = 0
        backtrack(0, "")
        return ans