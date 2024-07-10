class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for x in logs:
            if x == '../':
                if stack:
                    stack.pop()
                else:
                    continue
            elif x =='./':
                continue
            else:
                stack.append(x)
        return len(stack)