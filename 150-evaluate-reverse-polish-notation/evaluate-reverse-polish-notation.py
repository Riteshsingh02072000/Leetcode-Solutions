class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = '+-*/'

        for x in tokens:
            if x in operations:
                first = int(stack.pop())
                second = int(stack.pop())
                if x == '+':
                    cur = first + second
                elif x == '-':
                    cur = second - first
                elif x == '*':
                    cur = first*second
                elif x == '/':
                    cur = int(second/first)
                stack.append(cur)
            else:
                stack.append(x)
        return int(stack[-1])
