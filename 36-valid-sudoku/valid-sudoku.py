class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur == ".":
                    continue
                if cur in row[i] or cur in col[j] or cur in square[(i//3, j//3)]:
                    return False
                row[i].add(cur)
                col[j].add(cur)
                square[(i//3, j//3)].add(cur)
        return True