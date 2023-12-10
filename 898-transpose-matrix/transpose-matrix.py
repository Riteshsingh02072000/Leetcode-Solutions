class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        mat = [[0]*n for _ in range(len(matrix[0]))]

        for r in range(n):
            for c in range(len(matrix[0])):
                mat[c][r] = matrix[r][c]
        return mat