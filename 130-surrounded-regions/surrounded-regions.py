class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        q = deque()
        visited = set()
        direction = [0, 1, 0, -1, 0]

        for i in range(m):
            if board[i][0] == 'O':
                q.append([i, 0])
            if board[i][n-1] == 'O':
                q.append([i, n-1])
        
        for i in range(1, n-1):
            if board[0][i] == 'O':
                q.append([0, i])
            if board[m-1][i] == 'O':
                q.append([m-1, i])
        
        def inBound(i, j):
            return 0<=i<m and 0<=j<n

        while q:
            r, c = q.popleft()
            visited.add((r, c))
            for i in range(4):
                nr = r + direction[i]
                nc = c + direction[i+1]
                if inBound(nr, nc) and (nr, nc) not in visited and board[nr][nc] == 'O':
                    q.append([nr, nc])

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and board[i][j] == 'O':
                    board[i][j] = 'X'
