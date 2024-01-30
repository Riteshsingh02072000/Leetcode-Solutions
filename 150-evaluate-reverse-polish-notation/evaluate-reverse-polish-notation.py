class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = "+-*/"
        stack = []

        for x in tokens:

            if x not in operator:
                stack.append(x)
                continue
            first = int(stack.pop())
            second = int(stack.pop())
            if x=='+':
                ans = first+second
            elif x=='-':
                ans = second - first
            elif x=='*':
                ans = first*second
            else:
                ans = second/first
            stack.append(ans)
        return int(stack[0])