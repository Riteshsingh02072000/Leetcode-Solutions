class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        rtop, cleft = 0,0
        rbot = len(matrix)
        cright = len(matrix[0])

        while rtop<rbot and cleft<cright:
            for i in range(cleft, cright):
                ans.append(matrix[rtop][i])
            rtop+=1


            for i in range(rtop, rbot):
                ans.append(matrix[i][cright-1])
            cright-=1
            if not (rtop<rbot and cleft<cright):
                break


            for i in range(cright-1, cleft-1,-1):
                ans.append(matrix[rbot-1][i])
            rbot-=1


            for i in range(rbot-1, rtop-1, -1):
                ans.append(matrix[i][cleft])
            cleft+=1
        return ans