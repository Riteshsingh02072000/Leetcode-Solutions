class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used, res):
            if len(path) == len(nums):
                res.append(path.copy())
                return
            for i, letter in enumerate(nums):
                if used[i]:
                    continue
                path.append(letter)
                used[i] = True
                dfs(path, used, res)
                path.pop()
                used[i] = False
        
        ans = []
        dfs([], [False]*len(nums), ans)
        return ans