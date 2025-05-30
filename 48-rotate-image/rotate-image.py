class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l, r = 0, n-1
        while l<r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l+=1
            r-=1

        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        