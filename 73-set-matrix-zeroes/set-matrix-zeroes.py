class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # seenR = set()
        # seenC = set()
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if matrix[i][j] == 0:
        #             seenR.add(i)
        #             seenC.add(j)
        
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         if i in seenR or j in seenC:
        #             matrix[i][j] = 0

        valid = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    valid.append((i,j))
        for row, col in valid:
            matrix[row] = [0]*len(matrix[0])

            for i in range(len(matrix)):
                matrix[i][col] = 0

