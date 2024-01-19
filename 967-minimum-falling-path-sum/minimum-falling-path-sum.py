class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        for r in range(1,m):
            for c in range(n):
                if c==0:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1])
                elif c==n-1:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c-1])
                else:
                    matrix[r][c] += min(matrix[r-1][c], matrix[r-1][c+1], matrix[r-1][c-1])
        return min(matrix[-1])