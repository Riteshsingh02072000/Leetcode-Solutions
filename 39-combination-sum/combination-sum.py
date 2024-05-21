class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i, path):
            if sum(path) == target:
                ans.append(path.copy())
                return
            elif sum(path)>target:
                return
            
            for j in range(i, len(candidates)):
                dfs(j, path +[candidates[j]])
        dfs(0, [])
        return ans