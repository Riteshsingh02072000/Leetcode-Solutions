class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def checkArr(arr):
            arr.sort()
            
            diff = arr[1] - arr[0]
            ind = 1
            
            while ind < len(arr):
                if arr[ind] - arr[ind-1] != diff:
                    return False
                ind += 1
            
            return True
        
        ans = []
        for i in range(len(l)):
            val = checkArr(nums[l[i]:r[i]+1])
            ans.append(val)
        return ans