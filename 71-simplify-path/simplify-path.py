class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for x in path:
            if x=='' or x=='.':
                continue
            if x=='..':
                if stack:
                    stack.pop()
                continue
            else:
                stack.append(x)
        print(stack)
        return '/' + '/'.join(stack)

        # print(path)
        # return ""