class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        indegree =[0]*numCourses
        for u, v in prerequisites:
            indegree[u] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            if len(ans) == numCourses:
                return ans
            for ngbr in graph[course]:
                indegree[ngbr] -= 1
                if indegree[ngbr] == 0:
                    q.append(ngbr)
        return []

        
        
        
        
            
        #     for preq in graph[course]:
        #         indegrees[preq]-=1
        #         if indegrees[preq]==0:
        #             q.append(preq)
        # return []