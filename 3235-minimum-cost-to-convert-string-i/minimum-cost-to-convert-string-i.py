class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        arr = [[float('inf')]*26 for _ in range(26)]

        for i in range(26):
            arr[i][i] = 0
        
        for i in range(len(cost)):
            val1 = ord(original[i])-ord('a')
            val2 = ord(changed[i]) - ord('a')
            arr[val1][val2] = min(arr[val1][val2], cost[i])
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])
        
        ans = 0

        for i in range(len(source)):
            val1 = ord(source[i]) - ord('a')
            val2 = ord(target[i]) - ord('a')

            if val1 == val2:
                continue
            
            if arr[val1][val2] == float('inf'):
                return -1
            
            ans += arr[val1][val2]
        return ans