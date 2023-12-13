class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row =  collections.defaultdict(int)
        col =  collections.defaultdict(int)
        count = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row[i] += 1
                    col[j] += 1
                
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    if row[i]==1 and col[j]==1:
                        count+=1
        return count