class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w_count = collections.Counter(word)
        b_count = collections.defaultdict(int)

        n, m = len(board), len(board[0])
        for i in range(n):
            for j in range(m):
                b_count[board[i][j]] += 1

        for c in w_count:
            if b_count[c] < w_count[c]:
                return False
        
        def inBound(i, j):
            return 0<=i<n and 0<=j<m
        
        def dfs(word, board, r, c , index, visited):
            if index == len(word):
                return True
            
            visited.add((r,c))
            direction = [0, 1, 0, -1, 0]
            for i in range(4):
                nr = r + direction[i]
                nc = c + direction[i+1]

                if not inBound(nr, nc) or (nr,nc) in visited or board[nr][nc]!=word[index]:
                    continue
                if dfs(word, board, nr, nc, index+1, visited):
                    return True
            visited.remove((r, c))
            return False
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if dfs(word, board, i, j, 1, set()):
                        return True
        return False