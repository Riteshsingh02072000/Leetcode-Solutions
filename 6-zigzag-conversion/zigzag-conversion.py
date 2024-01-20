class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        ans = [[] for _ in range(numRows)]
        step = 1
        idx = 0
        for x in s:
            ans[idx].append(x)
            if idx==0:
                step = 1
            elif idx == numRows-1:
                step = -1
            idx+=step
        print(ans)
        ans = ["".join(x) for x in ans]
        return "".join(ans)
        # return "".join("".join(x for x in ans))