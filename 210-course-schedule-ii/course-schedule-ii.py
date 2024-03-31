class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
        
        indegrees = [0]*numCourses
        for u, v in prerequisites:
            indegrees[u] +=1
        
        q = deque()
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)
            if len(ans) == numCourses:
                return ans
            
            for preq in graph[course]:
                indegrees[preq]-=1
                if indegrees[preq]==0:
                    q.append(preq)
        return []