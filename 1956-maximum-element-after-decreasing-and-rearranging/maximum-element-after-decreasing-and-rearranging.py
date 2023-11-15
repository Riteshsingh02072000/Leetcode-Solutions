class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        # return len(list(set(arr)))

        arr.sort()
        ans = 1
        for i in range(1, len(arr)):
            if arr[i]>ans:
                ans+=1
        return ans