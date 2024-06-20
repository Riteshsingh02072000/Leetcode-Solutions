class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        pos.sort()
        l, r = 1, (pos[-1]-pos[0])//(m-1)

        ans = -1

        while l<=r:
            mid = (l+r)//2
            last_pos, balls = pos[0], 1
            for i in range(1, len(pos)):
                if pos[i]-last_pos>=mid:
                    balls+=1
                    last_pos = pos[i]
            
            if balls>=m:
                ans = mid
                l = mid+1
            else:
                r = mid - 1
        return ans