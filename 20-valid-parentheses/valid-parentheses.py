class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for x in s:
            if stack and x == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and x == ']' and stack[-1] =='[':
                stack.pop()
            elif stack and x == '}' and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(x)
        return not stack