class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        visited = [float('inf')]*n
        visited[src] = 0

        for x in flights:
            graph[x[0]].append((x[1], x[2]))
        
        q = deque([(src, 0)])
        k+=1

        while k>0 and q:
            for i in range(len(q)):
                cur_airport, cur_price = q.popleft()
                for ngbr, price in graph[cur_airport]:
                    np = price+cur_price
                    if visited[ngbr]>np:
                        visited[ngbr] = np
                        q.append((ngbr, np))
            k-=1
        return visited[dst] if visited[dst]!=float('inf') else -1