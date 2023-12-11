class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return arr[0]

        count = 1
        for i in range(1, len(arr)):
            if arr[i]==arr[i-1]:
                count+=1
                if count >( n/4):
                    return arr[i]
            else:
                count = 1
        return -1