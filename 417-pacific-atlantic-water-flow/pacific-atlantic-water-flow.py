class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        ans = []

        def inBound(i, j):
            return 0<=i<m and 0<=j<n
        
        def isPacific(r, c, prev, visited):
            if not inBound(r, c):
                return False
            if (r, c) in visited or heights[r][c]>prev:
                return False
            
            visited.add((r, c))

            if r == 0 or c == 0:
                return True
            
            return (isPacific(r+1, c, heights[r][c], visited) or isPacific(r-1, c, heights[r][c], visited) or isPacific(r, c+1, heights[r][c], visited) or isPacific(r, c-1, heights[r][c], visited))


        def isAtlantic(r, c, prev, visited):
            if not inBound(r, c):
                return False
            if (r, c) in visited or heights[r][c]>prev:
                return False
            
            visited.add((r, c))

            if r == m-1 or c == n-1:
                return True
            
            return (isAtlantic(r+1, c, heights[r][c], visited) or isAtlantic(r-1, c, heights[r][c], visited) or isAtlantic(r, c+1, heights[r][c], visited) or isAtlantic(r, c-1, heights[r][c], visited))

        
        for i in range(m):
            for j in range(n):
                if isPacific(i, j, heights[i][j], set()) and isAtlantic(i, j, heights[i][j], set()):
                    ans.append([i, j])
        return ans