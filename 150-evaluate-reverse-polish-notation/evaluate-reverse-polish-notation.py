class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = '+-*/'
        stack = []
        for x in tokens:
            if x in operator:
                second = stack.pop()
                first = stack.pop()
                if x == '+':
                    stack.append(first+second)
                elif x == '-':
                    stack.append(first-second)
                elif x=='*':
                    stack.append(first*second)
                else:
                    stack.append(int(first/second))
            else:
                # print(int(x))
                stack.append(int(x))
        return stack[-1]
