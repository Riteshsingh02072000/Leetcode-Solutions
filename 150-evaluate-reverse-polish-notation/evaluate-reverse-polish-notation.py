class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = "+-*/"
        stack = []

        for x in tokens:
            if x in operator:
                first = int(stack.pop())
                second = int(stack.pop())
                if x == '+':
                    ans = first+second
                elif x=='-':
                    ans = second - first
                elif x=='*':
                    ans = first*second
                elif x=='/':
                    ans = second/first
                stack.append(ans)
            else:
                stack.append(int(x))
        return int(stack[0])