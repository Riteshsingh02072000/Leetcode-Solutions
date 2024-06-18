class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = [[d, p] for d,p in zip(difficulty, profit)]
        jobs.sort()

        mx_profit = jobs[0][1]

        for i in range(1, len(jobs)):
            mx_profit = max(mx_profit, jobs[i][1])
            jobs[i][1] = mx_profit
        
        ans = 0
        for w in worker:
            ans += self.binarySearch(jobs, w)
        return ans
    
    def binarySearch(self, arr, w):
        l, r = 0, len(arr)

        while l<r:
            mid = (l+r)//2
            if arr[mid][0]<=w:
                l = mid+1
            else:
                r = mid
        
        if l == 0:
            return 0
        return arr[l-1][1]