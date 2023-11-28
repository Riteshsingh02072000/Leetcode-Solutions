class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        mat = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                cur = board[i][j]
                if cur==".":
                    continue
                if cur in rows[i] or cur in cols[j] or cur in mat[(i//3, j//3)]:
                    return False
                
                rows[i].add(cur)
                cols[j].add(cur)
                mat[(i//3, j//3)].add(cur)
        return True