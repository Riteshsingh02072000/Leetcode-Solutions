class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(i, path, ans):
            if sum(path) == target:
                if path not in ans:
                    ans.append(path.copy())
                return
            
            elif sum(path)>target:
                return
            
            prev = -1
            for j in range(i, len(candidates)):
                if candidates[j] == prev:
                    continue
                path.append(candidates[j])
                backtrack(j+1, path, ans)
                path.pop()
                prev = candidates[j]
        
        backtrack(0, [], ans)
        return ans

