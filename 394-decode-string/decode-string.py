class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for x in s:
            if x!=']':
                stack.append(x)
            else:
                substring = ""
                while stack[-1]!='[':
                    substring = stack.pop() + substring
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(substring*int(num))
        return ''.join(stack)