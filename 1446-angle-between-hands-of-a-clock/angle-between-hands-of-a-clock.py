class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hourAngle = hour*30 + 0.5*minutes
        minuteAngle = 6*minutes

        diff = abs(hourAngle - minuteAngle)
        return min(diff, 360-diff)