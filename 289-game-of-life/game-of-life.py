class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        # m , n = len(board), len(board[0])
        # def inbound(r,c):
        #     return 0<=r<m and 0<=c<n
        # # def count(r,c):
        # #     val = (
        # #         (board[r+1][c] if r<m-1 else 0 )+
        # #         (board[r-1][c] if r>0 else 0)+
        # #         (board[r-1][c-1] if r>0 and c>0 else 0)+
        # #         (board[r-1][c+1] if r>0 and c<n-1 else 0)+
        # #         (board[r][c-1] if c>0 else 0 )+
        # #         (board[r][c+1] if c<n-1 else 0) +
        # #         (board[r+1][c-1] if r<m-1 and c>0 else 0 )+ 
        # #         (board[r+1][c+1] if r<m-1 and c<n-1 else 0)
        # #     )
        # #     return val
        # x = product([-1, 0, 1], [-1, 0, 1])
        # for r, c in product([-1, 0,1], [-1, 0, 1]):
        #     print((r,c))
        # # print(x)
        # directions = set((x,y) for x in (-1,0,1) for y in (-1,0,1) if x or y)
        # print(directions)
        # tmp = collections.defaultdict(int)
        # for r in range(m):
        #     for c in range(n):
        #         count = 0
        #         for x,y in directions:
        #             nr = r+x
        #             nc = c+y
        #             if inbound(nr, nc):
        #                 count += board[nr][nc]
        #         # ngbr = count(r,c)
        #         if count<2 or count>3:
        #             if board[r][c] ==1:
        #                 tmp[(r,c)] = 0
        #         if count==3 and board[r][c]==0:
        #             tmp[(r,c)] = 1
        
        # for key, val in tmp.items():
        #     x, y = key
        #     board[x][y] = val
        # return board


        row, col = len(board), len(board[0])
        tmp = collections.defaultdict(int)

        def inBound(r, c):
            return 0<=r<row and 0<=c<col
        
        for r in range(row):
            for c in range(col):
                count = 0
                for x, y in product([-1, 0, 1], [-1, 0, 1]):
                    if x==0 and y==0:
                        continue
                    nr = r+x
                    nc = c+y
                    if inBound(nr, nc):
                        count+=board[nr][nc]
                if (count<2 or count>3) and board[r][c]==1:
                    tmp[(r,c)] = 0
                elif count == 3 and board[r][c]==0:
                    tmp[(r,c)] = 1
        
        for key, v in tmp.items():
            r, c = key
            board[r][c] = v
        


                