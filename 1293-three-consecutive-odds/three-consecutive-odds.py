class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        # cur = 0
        # for x in arr:
        #     if x%2==1:
        #         cur += 1
        #     else:
        #         cur = 0
            
        #     if cur == 3:
        #         return True
        # return False

        ans = 0
        for i in range(min(3, len(arr))):
            ans += arr[i]%2
        
        if ans == 3:
            return True
        
        for i in range(3, len(arr)):
            ans += arr[i]%2
            ans -= arr[i-3]%2
            if ans == 3:
                return True
        return False


            