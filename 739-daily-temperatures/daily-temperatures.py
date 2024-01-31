class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)-1, -1, -1):
            t = temperatures[i]
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]]<=t:
                    stack.pop()
                if stack:
                    ans[i] = stack[-1] - i
                stack.append(i)
        return ans