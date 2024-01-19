class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        

        m , n = len(board), len(board[0])
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
        # def count(r,c):
        #     val = (
        #         (board[r+1][c] if r<m-1 else 0 )+
        #         (board[r-1][c] if r>0 else 0)+
        #         (board[r-1][c-1] if r>0 and c>0 else 0)+
        #         (board[r-1][c+1] if r>0 and c<n-1 else 0)+
        #         (board[r][c-1] if c>0 else 0 )+
        #         (board[r][c+1] if c<n-1 else 0) +
        #         (board[r+1][c-1] if r<m-1 and c>0 else 0 )+ 
        #         (board[r+1][c+1] if r<m-1 and c<n-1 else 0)
        #     )
        #     return val
        directions = set((x,y) for x in (-1,0,1) for y in (-1,0,1) if x or y)
        print(directions)
        tmp = collections.defaultdict(int)
        for r in range(m):
            for c in range(n):
                count = 0
                for x,y in directions:
                    nr = r+x
                    nc = c+y
                    if inbound(nr, nc):
                        count += board[nr][nc]
                # ngbr = count(r,c)
                if count<2 or count>3:
                    if board[r][c] ==1:
                        tmp[(r,c)] = 0
                if count==3 and board[r][c]==0:
                    tmp[(r,c)] = 1
        
        for key, val in tmp.items():
            x, y = key
            board[x][y] = val
        return board
                