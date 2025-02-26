class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        graph = {i: [] for i in range(n)}

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobpath = [-1]*n
        path = []

        def getBobPath(node, parent):
            if node == 0:
                return True
            for ngbr in graph[node]:
                if ngbr!=parent:
                    path.append(node)
                    if getBobPath(ngbr, node):
                        return True
                    path.pop()
        getBobPath(bob, -1)
        for i, node in enumerate(path):
            bobpath[node] = i


        def getAliceScore(node, parent, score, time):
            if bobpath[node] == -1 or bobpath[node]>time:
                score += amount[node]
            elif bobpath[node] == time:
                score += amount[node]//2
            
            return score if len(graph[node]) ==1 and node!=0 else max(getAliceScore(ngbr, node, score, time+1) for ngbr in graph[node] if ngbr!=parent)
        return getAliceScore(0, -1, 0, 0)
