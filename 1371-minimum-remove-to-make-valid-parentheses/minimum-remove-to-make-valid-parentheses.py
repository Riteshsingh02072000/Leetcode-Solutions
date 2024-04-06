class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                    continue
                else:
                    stack.append(i)
        
        ans = []
        
        for i,char in enumerate(s):
            if stack and stack[0] == i:
                stack.pop(0)
                continue
            ans.append(char)
        return ans