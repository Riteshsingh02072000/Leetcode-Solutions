class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        ans = ['.' for _ in range(n)]
        q = deque()

        for i, d in enumerate(dominoes):
            if d == 'L' or d == 'R':
                q.append((i, d))
            ans[i] = d
        
        while q:
            collision = defaultdict(list)
            for _ in range(len(q)):
                i, d = q.popleft()
                if d == 'L' and i-1>=0 and ans[i-1] == '.':
                    collision[i-1].append(d)
                elif d == 'R' and i+1<n and ans[i+1] == '.':
                    collision[i+1].append(d)
                
            for pos in collision:
                if len(collision[pos]) == 2:
                    ans[pos] = "."
                else:
                    ans[pos] = collision[pos][0]
                    q.append((pos, collision[pos][0]))
        return ''.join(ans)