class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indegree = [0] * n
        length = [0] * n
        for i, x in enumerate(favorite):
            indegree[x] += 1
        que = collections.deque([i for i in range(n) if indegree[i] == 0])
        while que:
            cur = que.popleft()
            nxt = favorite[cur]
            indegree[nxt] -= 1
            length[nxt] = max(length[nxt], length[cur] + 1)
            if indegree[nxt] == 0:
                que.append(nxt)
        smallring = 0
        bigring = 0
        for i in range(n):
            if indegree[i] > 0:
                size = 1
                indegree[i] -= 1
                nxt = favorite[i]
                while nxt != i:
                    indegree[nxt] -= 1
                    size += 1
                    nxt = favorite[nxt]
                if size == 2:
                    smallring += length[i] + length[favorite[i]] + 2
                else:
                    bigring = max(bigring, size)
        return max(smallring, bigring) 
