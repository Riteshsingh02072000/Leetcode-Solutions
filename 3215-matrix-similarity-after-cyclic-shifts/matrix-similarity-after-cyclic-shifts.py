class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k%n
        tmp = [row[:] for row in mat]
        # print(mat[0][-1:], mat[0][:-1])
        for i in range(k):
            for j in range(m):
                if j %2==0:
                    mat[j] = mat[j][1:] + mat[j][:1]
                elif j%2!=0:
                    mat[j] = mat[j][-1:] + mat[j][:-1]
        return tmp == mat
