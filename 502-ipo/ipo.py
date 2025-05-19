class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        heap = []
        project = [[p, c] for p, c in zip(profits, capital)]
        project = sorted(project, key = lambda x:x[1])
        print(project)
        i = 0
        for _ in range(k):
            while i<len(project) and w>=project[i][1]:
                heapq.heappush(heap, -project[i][0])
                i+=1
            if heap:
                w += -(heapq.heappop(heap))
        return w