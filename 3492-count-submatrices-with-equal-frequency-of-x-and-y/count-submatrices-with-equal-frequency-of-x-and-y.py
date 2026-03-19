class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        ans = 0
        sumx =[0]*c
        sumy = [0]*c

        for i in range(r):
            nx = 0
            ny = 0

            for j in range(c):
                if grid[i][j] == 'X':
                    nx+=1
                if grid[i][j] == 'Y':

                    ny+=1
                
                sumx[j] += nx
                sumy[j] += ny

                if sumx[j]>0 and sumx[j]==sumy[j]:
                    ans+=1
        return ans