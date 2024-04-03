class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        w_count = collections.Counter(word)
        b_count = collections.defaultdict(int)

        
    

        def inBound(i, j):
            return 0<=i<len(board) and 0<=j<len(board[0])

        
        def dfs(board, r,c, index, word, visited):
            if index == len(word):
                return True
            visited.add((r,c))
            direction = [0,1,0,-1,0]

            for i in range(4):
                nr = r+direction[i]
                nc = c + direction[i+1]

                if not inBound(nr, nc) or (nr,nc) in visited or board[nr][nc]!=word[index]:
                    continue
                if dfs(board, nr,nc,index+1, word, visited):
                    return True
            
            visited.remove((r,c))

            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                b_count[board[r][c]] += 1
        
        for c in w_count:
            if w_count[c]>b_count[c]:
                return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]==word[0]:
                    if dfs(board, r,c, 1, word, set()):
                        return True
        
        return False

