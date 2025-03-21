class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = collections.defaultdict(list)
        ing = collections.defaultdict(int)

        for i in range(len(ingredients)):
            for j in range(len(ingredients[i])):
                adj[ingredients[i][j]].append(recipes[i])
                ing[recipes[i]]+=1
        
        ans = []
        q = collections.deque()
        for i in range(len(supplies)):
            q.append(supplies[i])

        while q:
            cur = q.popleft()
            for i in adj[cur]:
                ing[i]-=1
                if ing[i]==0:
                    q.append(i)
                    ans.append(i)
        return ans
