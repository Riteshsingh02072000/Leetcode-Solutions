class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        if not s:
            return 0
        for x in s:
            if stack and ((x == ')' and stack[-1] == '(') ):
                stack.pop()
            else:
                stack.append(x)
        
        return len(stack)
