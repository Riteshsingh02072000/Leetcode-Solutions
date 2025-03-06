class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        missing = (n*n)*(1+n*n)//2
        seen = set()
        duplicate = -1

        for row in grid:
            for x in row:
                if x not in seen:
                    seen.add(x)
                    missing -= x
                else:
                    duplicate = x
        return [duplicate, missing]