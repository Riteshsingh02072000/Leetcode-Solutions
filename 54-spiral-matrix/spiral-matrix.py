class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        cleft, rtop = 0,0
        cright, rbottom = len(matrix[0]), len(matrix)

        while rtop<rbottom and cleft<cright:
            for i in range(cleft, cright):
                ans.append(matrix[rtop][i])
            rtop+=1

            for i in range(rtop, rbottom):
                ans.append(matrix[i][cright-1])
            cright -= 1

            if not (rtop<rbottom and cleft<cright):
                break
            
            for i in range(cright-1, cleft-1, -1):
                ans.append(matrix[rbottom-1][i])
            rbottom -= 1

            for i in range(rbottom-1, rtop-1, -1):
                ans.append(matrix[i][cleft])
            cleft+=1
        return ans