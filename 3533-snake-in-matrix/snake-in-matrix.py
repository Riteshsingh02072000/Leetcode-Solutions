class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        moves = {'UP': (-1, 0), 'DOWN': (1, 0), 'RIGHT': (0, 1), 'LEFT': (0, -1)}

        curR, curC = 0, 0
        for x in commands:
            nr, nc = moves[x]
            curR = curR + nr
            curC = curC + nc
        return (curR*n) + curC