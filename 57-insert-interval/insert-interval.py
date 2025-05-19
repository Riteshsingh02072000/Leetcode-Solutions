class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        prefix, suffix = [], []
        start, end = newInterval

        for x in intervals:
            if x[1]<start:
                prefix.append(x)
            elif x[0]>end:
                suffix.append(x)
            else:
                start = min(start, x[0])
                end = max(end, x[1])
        return prefix + [[start, end]] + suffix
