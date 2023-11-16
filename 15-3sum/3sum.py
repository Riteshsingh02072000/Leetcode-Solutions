class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)-2):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            
            while j<k:
                add = nums[i] + nums[j] + nums[k]

                if add == 0:
                    if [nums[i], nums[j], nums[k]] not in ans:
                        ans.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                
                elif add>0:
                    k-=1
                else:
                    j+=1
        return ans