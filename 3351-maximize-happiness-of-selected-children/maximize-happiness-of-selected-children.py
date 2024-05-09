class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans= 0
        cur =0 
        happiness.sort(reverse = True)
        for i in range(k):
            ans+=max(0, (happiness[i]-cur))
            cur+=1
        return ans