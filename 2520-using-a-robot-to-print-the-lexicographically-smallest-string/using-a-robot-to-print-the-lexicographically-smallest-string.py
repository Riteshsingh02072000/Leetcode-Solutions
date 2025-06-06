class Solution:
    def robotWithString(self, s: str) -> str:
        dic = Counter(s)
        ans = []
        stack = [] #t or stack

        for char in s:
            stack.append(char)
            if dic[char] == 1:
                del dic[char]
            else:
                dic[char] -= 1
            while dic and stack and min(dic) >= stack[-1]:
                ans.append(stack.pop())
        ans += stack[::-1]
        return ''.join(ans)