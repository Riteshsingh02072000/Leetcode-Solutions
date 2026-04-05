class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x, y = 0, 0
        direction = {'R': (0, 1), 'L': (0, -1), 'U': (-1, 0), 'D': (1, 0)}

        for move in moves:
            nx, ny = direction[move]
            x += nx
            y += ny
        return x==0 and y==0