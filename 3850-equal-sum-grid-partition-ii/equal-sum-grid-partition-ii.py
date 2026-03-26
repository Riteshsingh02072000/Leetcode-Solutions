class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(g):
            m, n = len(g), len(g[0])
            if m<2:
                return False
            bot_freq = Counter()
            for r in range(m):
                for c in range(n):
                    bot_freq[g[r][c]] += 1
            
            top_freq = Counter()
            row_sum = [sum(row) for row in g]
            total = sum(row_sum)
            top_sum = 0

            for r in range(m-1):
                for c in range(n):
                    val = g[r][c]
                    top_freq[val] += 1
                    bot_freq[val] -= 1
                    if bot_freq[val] == 0: del bot_freq[val]
                
                top_sum += row_sum[r]
                bot_sum = total - top_sum
                if top_sum == bot_sum:
                    return True
                diff = abs(top_sum-bot_sum)
                if top_sum>bot_sum:
                    if r==0:
                        if diff == g[0][0] or diff == g[0][n-1]:
                            return True
                    elif n == 1:
                        if diff == g[0][0] or diff == g[r][0]:
                            return True
                    elif diff in top_freq:
                        return True
                else:
                    bot_row = m-r-1
                    if bot_row == 1:
                        if diff == g[r+1][0] or diff == g[r+1][n-1]:
                            return True
                    elif n==1:
                        if diff == g[r+1][0] or diff == g[m-1][0]:
                            return True
                    elif diff in bot_freq:
                        return True
            return False
        
        if check(grid):
            return True
        transposed = [[grid[r][c] for r in range(len(grid))] for c in range(len(grid[0]))]
        return check(transposed)