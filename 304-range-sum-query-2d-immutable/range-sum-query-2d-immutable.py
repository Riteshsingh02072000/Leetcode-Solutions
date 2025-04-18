class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m , n = len(matrix), len(matrix[0])
        self.sumMat = [[0]*(n+1) for _ in range(m+1)]
        for r in range(m):
            prefix = 0
            for c in range(n):
                prefix+=matrix[r][c]
                self.sumMat[r+1][c+1] = prefix + self.sumMat[r][c+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2, c1, c2 = row1+1, row2+1, col1+1, col2+1
        bottomRight = self.sumMat[r2][c2]
        above = self.sumMat[r1-1][c2]
        left = self.sumMat[r2][c1-1]
        topLeft = self.sumMat[r1-1][c1-1]
        return bottomRight - above - left + topLeft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)