class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        l, r = 0, len(height)-1

        while l<r:
            ans = max(ans, min(height[l], height[r])*(r-l))
            if height[l]>height[r]:
                r -= 1
            else:
                l+=1
        return ans