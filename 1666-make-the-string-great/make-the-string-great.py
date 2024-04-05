class Solution:
    def makeGood(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        ans = ''
        for x in s:
            
            if (stack and (stack[-1].isupper() and (stack[-1].lower() == x))):
                stack.pop()
            elif (stack and (stack[-1].islower() and (stack[-1].upper() == x))):
                stack.pop()
            else:
                stack.append(x)
         
        for y in stack:
            ans += str(y)
            
        return ans