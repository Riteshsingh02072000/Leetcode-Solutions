class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums_list = [str(num) for num in nums]
        nums_list.sort(reverse = True)
        ans = ""

        def helper(left, right):
            if ans + nums_list[left]+nums_list[right]< ans+nums_list[right]+nums_list[left]:
                nums_list[left], nums_list[right] = nums_list[right], nums_list[left]
            return
    


        for i in range(len(nums_list)):
            r = i+1
            while r<len(nums_list) and nums_list[i][0] == nums_list[r][0]:
                helper(i,r)
                r+=1
            ans+= nums_list[i]
        if int(ans)==0:
            return "0"
        return ans
