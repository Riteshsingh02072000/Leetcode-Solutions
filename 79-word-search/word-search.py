class Solution:
    def exist(self, grid: List[List[str]], word: str) -> bool:
        m, n = len(grid), len(grid[0])
        wordCount = Counter(word)
        gridCount = defaultdict(int)

        for i in range(m):
            for j in range(n):
                gridCount[grid[i][j]] += 1
        
        for c in wordCount:
            if wordCount[c]>gridCount[c]:
                return False
        directions = [0,1,0, -1, 0]

        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        
        def dfs(r, c, index, visited):
            if index == len(word):
                return True
            
            visited.add((r,c))
            for i in range(4):
                nr = r + directions[i]
                nc = c + directions[i+1]
                if not inBound(nr, nc) or (nr, nc) in visited or grid[nr][nc]!=word[index]:
                    continue
                if dfs(nr, nc, index+1, visited):
                    return True
            visited.remove((r, c))
            return False
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == word[0]:
                    if dfs(i, j, 1, set()):
                        return True
        return False