class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = keysPressed[0]
        n = len(releaseTimes)
        mx = releaseTimes[0]
        for i in range(1, n):
            if (releaseTimes[i]-releaseTimes[i-1])>=mx:
                if mx == releaseTimes[i]-releaseTimes[i-1]:
                    ans = chr(max(ord(ans), ord(keysPressed[i])))
                else:
                    mx = releaseTimes[i]-releaseTimes[i-1]
                    ans = keysPressed[i]
        return ans

        # max_heap = [(-releaseTimes[0],-ord(keysPressed[0]), keysPressed[0])]
        # # curr_time 
        # for i in range(1,len(releaseTimes)):
        #     curr_time = releaseTimes[i] - releaseTimes[i-1]
        #     # Flip the second key by negating the ASCII value of the key
        #     heapq.heappush(max_heap, (-curr_time, -ord(keysPressed[i]), keysPressed[i]))

                           
                        
        # print(max_heap)
        
        # top_duration, top_key, t = heapq.heappop(max_heap)
        # return t