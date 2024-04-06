class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = list(range(1, n+1))
        # print(arr)
        ans = []

        def backtrack(i, cur):
            if i == n:
                if len(cur) == k:
                    ans.append(cur.copy())
                    return
            else:
                cur.append(arr[i])
                backtrack(i+1, cur)
                cur.pop()
                backtrack(i+1, cur)
        backtrack(0, [])
        return ans
        
        