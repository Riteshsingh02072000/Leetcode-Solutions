class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0
        def timeConvert(x):
            hour, minutes = map(int, x.split(':'))
            return hour*60 + minutes
        

        minutes = [timeConvert(tp) for tp in timePoints]
        minutes.sort()
        minDiff = float('inf')

        for i in range(1, len(minutes)):
            minDiff = min(minDiff, minutes[i] - minutes[i-1])
        
        circular = 1440 - minutes[-1] + minutes[0]
        return min(minDiff, circular)
