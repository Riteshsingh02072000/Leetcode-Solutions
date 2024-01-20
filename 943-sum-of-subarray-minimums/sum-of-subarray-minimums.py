class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        n = len(arr)
        dp = [0]*n
        ans = 0
        mod = 10**9 + 7


        for i in range(n):
            while stack and arr[i]<=arr[stack[-1]]:
                stack.pop()
            
            if stack:
                j = stack[-1]
                dp[i] = dp[j] + arr[i]*(i-j)
            else:
                dp[i] = arr[i]*(i+1)
            stack.append(i)
            ans = (ans+dp[i])%mod
        return ans