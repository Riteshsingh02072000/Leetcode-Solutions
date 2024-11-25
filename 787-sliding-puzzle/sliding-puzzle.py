class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        target = '123450'
        start = ''.join(str(num) for row in board for num in row)

        neighbor = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5:[2,4]
        }

        q = deque([(start, 0)])

        visited = set()
        visited.add(start)

        while q:
            cur, move = q.popleft()
            if cur == target:
                return move
            
            idx = cur.index('0')

            for ngbr in neighbor[idx]:
                new_cur = list(cur)
                new_cur[ngbr], new_cur[idx] = new_cur[idx], new_cur[ngbr]
                
                new_cur = ''.join(new_cur)
                if new_cur not in visited:
                    visited.add(new_cur)
                    q.append((new_cur, move+1))
        return -1