class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        self.count = 0
        self.part = []

        def isSafe(part, x):
            for n in part:
                if abs(n-x)==k:
                    return False
            return True
        
        def subsetArr(i):
            if i>=len(nums):
                self.count+=1
                return
            
            if isSafe(self.part, nums[i]):
                self.part.append(nums[i])
                subsetArr(i+1)
                self.part.pop()
                
            subsetArr(i+1)
        subsetArr(0)
        return self.count-1