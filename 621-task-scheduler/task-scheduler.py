class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n ==0:
            return len(tasks)
        d = defaultdict(int)
        for x in tasks:
            d[x]+=1

        h = []
        for k,v in d.items():
            heapq.heappush(h, (-v, k))

        ans = 0
        while h:
            tmp = []
            for i in range(n+1):
                ans+=1
                if h:
                    v, key = heapq.heappop(h)
                    if v!=-1:
                        tmp+=[(v+1, k)]
                if not h and not tmp:
                    return ans
            for t in tmp:
                heapq.heappush(h, t)
        return ans    