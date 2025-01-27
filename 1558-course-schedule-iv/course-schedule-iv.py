class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        prereq = defaultdict(list)
        for x, y in prerequisites:
            prereq[y].append(x)
        
        ans = []
        memo ={}

        def dfs(course, prer):
            if (course, prer) in memo:
                return memo[(course, prer)]
            
            for p in prereq[course]:
                if p == prer or dfs(p, prer):
                    memo[(course, prer)] = True
                    return True
            
            memo[(course, prer)] = False
            return False
        return [dfs(query[1], query[0]) for query in queries]