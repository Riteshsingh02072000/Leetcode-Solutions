class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def getPos(pos):
            row = (pos-1)//n
            col = (pos-1)%n
            
            if row%2==1:
                col = n - 1 - col
            row = n-1-row
            return row, col
        
        visited = set()
        q = deque([(1, 0)])

        while q:
            pos, moves = q.popleft()
            for i in range(1, 7):
                newPos = pos + i
                if newPos > n*n:
                    break
                r, c = getPos(newPos)
                if board[r][c] != - 1:
                    newPos = board[r][c]
                if newPos == n*n:
                    return moves+1
                if newPos not in visited:
                    visited.add(newPos)
                    q.append((newPos, moves + 1))
        return -1