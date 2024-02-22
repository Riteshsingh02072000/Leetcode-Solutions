class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ingoing = [0]*(n+1)
        outgoing = [0]*(n+1)

        for x,y in trust:
            ingoing[x]+=1
            outgoing[y] +=1
        for i in range(1, n+1):
            if ingoing[i] == 0 and outgoing[i] == n-1:
                return i
        return -1
