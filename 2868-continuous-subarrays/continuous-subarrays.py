from sortedcontainers import SortedList
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_window = SortedList()
        l = 0
        ans = 0


        for r in range(n):
            sorted_window.add(nums[r])

            while sorted_window[-1]-sorted_window[0] > 2:
                sorted_window.remove(nums[l])
                l+=1
            ans += r - l+1
        return ans