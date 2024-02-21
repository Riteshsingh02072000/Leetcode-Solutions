class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        cur = 0
        sign = 1
        ans= 0 
        for c in s:
            if c.isdigit():
                cur = (10*cur)+int(c)
            elif c in '+-':
                ans += sign*cur
                sign = -1 if c=='-' else 1
                cur = 0

            elif c=='(':
                stack.append(ans)
                stack.append(sign)
                # cur = 0
                ans = 0
                sign =1

            elif c==')':
                ans+=sign*cur
                ans*=stack.pop()
                ans+=stack.pop()
                cur = 0
        return ans + sign*cur




