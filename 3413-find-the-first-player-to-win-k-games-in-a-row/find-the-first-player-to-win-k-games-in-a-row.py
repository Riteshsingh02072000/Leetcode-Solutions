class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        # win = defaultdict(int)
        # player = [i for i in range(len(skills))]

        # while 1:
        #     first, second = player[0], player[1]
        #     if skills[first]>skills[second]:
        #         player.append(player.pop(second))
        #         win[first] += 1
        #         if win[first] == k:
        #             return first
        #     else:
        #         player.append(player.pop(first))
        #         win[second] += 1
        #         if win[second] == k:
        #             return second

        n = len(skills)
        q = deque(range(1, n))
        ele = 0
        win = 0

        while 1:
            num = q.popleft()
            if skills[num]<skills[ele]:
                win+=1
                q.append(num)
            else:
                win = 1
                q.append(ele)
                ele = num
            
            if win == k or win>=n-1:
                return ele
        