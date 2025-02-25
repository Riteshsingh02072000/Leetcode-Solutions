class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        bag = []
        for i, x in enumerate(grid):
            x.sort(reverse = True)
            bag += x[:limits[i]]
        bag.sort(reverse=True)
        return sum(bag[:k])
        
