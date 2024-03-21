class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        direction = [0, 1, 0, -1, 0]
        q = deque()
        # visited = set()

        for i in range(m):
            if board[i][0] == 'O':
                q.append([i, 0])
            if board[i][n-1] == 'O':
                q.append([i, n-1])
        
        for i in range(n):
            if board[0][i] == 'O':
                q.append([0, i])
            if board[m-1][i] == 'O':
                q.append([m-1, i])
        
        def inBound(r, c):
            return 0<=r<m and 0<=c<n
        
        while q:
            i, j = q.popleft()
            board[i][j] = '#'
            for x in range(4):
                nr = i + direction[x]
                nc = j + direction[x+1]

                if inBound(nr, nc) and board[nr][nc] == 'O':
                    q.append([nr, nc])
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'