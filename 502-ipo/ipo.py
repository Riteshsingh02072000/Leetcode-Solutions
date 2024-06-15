class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        projects = [[c,p] for c,p in zip(capital, profits
        )]
        projects.sort(key = lambda x:x[0])

        i = 0
        for x in range(k):
            while i<len(capital) and projects[i][0]<=w:
                heapq.heappush(heap, -projects[i][1])
                i+=1
            
            if heap:
                w -= heapq.heappop(heap)
        return w