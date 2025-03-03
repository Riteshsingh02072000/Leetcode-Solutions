class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # prefix = []
        # suffix = []
        # same = 0

        # for x in nums:
        #     if x<pivot:
        #         prefix.append(x)
        #     elif x>pivot:
        #         suffix.append(x)
        #     else:
        #         same+=1
        # return prefix + [pivot]*same + suffix
        n = len(nums)
        ans = [0]*n
        l, r = 0, n-1

        for i, j in zip(range(len(nums)), range(len(nums)-1, -1, -1)):
            if nums[i]<pivot:
                ans[l] = nums[i]
                l += 1
            if nums[j] > pivot:
                ans[r] = nums[j]
                r-=1
        
        while l<=r:
            ans[l] = pivot
            l+=1
        return ans