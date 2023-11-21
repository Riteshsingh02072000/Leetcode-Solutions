class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        prefix = []
        suffix = []
        for i in intervals:
            if i[1]<start:
                prefix.append(i)
            elif i[0]>end:
                suffix.append(i)
            else:
                start = min(start, i[0])
                end = max(i[1], end)
        return prefix+[[start, end]] + suffix         