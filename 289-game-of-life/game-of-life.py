class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        tmp = defaultdict(int)

        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        
        for i in range(m):
            for j in range(n):
                count = 0
                for x, y in product([-1, 0, 1], [-1, 0, 1]):
                    if x == 0 and y == 0:
                        continue
                    nr = i+x
                    nc = j+y

                    if inBound(nr, nc):
                        count += board[nr][nc]
                if (count>3 or count<2) and board[i][j] == 1:
                    tmp[(i, j)] = 0
                elif count == 3 and board[i][j] == 0:
                    tmp[(i, j)] = 1
        
        for key, val in tmp.items():
            x, y = key
            board[x][y] = val