class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        n = len(nums)

        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j = i +1
            k = n-1

            while j<k:
                add = nums[i] + nums[j] + nums[k]
                if add == 0:
                    ans.append((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1
                elif add > 0:
                    k-=1
                else:
                    j+=1
        return ans