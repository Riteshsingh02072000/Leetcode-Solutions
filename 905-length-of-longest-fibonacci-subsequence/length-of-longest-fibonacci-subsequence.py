class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        numSet = set(arr)
        ans = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                prev = arr[j]
                cur = arr[i] + prev
                curLen = 2

                while cur in numSet:
                    prev, cur = cur, cur+prev
                    curLen+=1
                    ans = max(ans, curLen)
        return ans 