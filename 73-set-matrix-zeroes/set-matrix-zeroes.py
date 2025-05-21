class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        valid = defaultdict(bool)

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    valid[(i, j)] = True
        

        for point in valid.keys():
            x, y = point
            matrix[x] = [0]*n

            for i in range(m):
                matrix[i][y] = 0
