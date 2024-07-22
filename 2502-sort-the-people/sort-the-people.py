class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        ans = []
        for x, y in sorted(zip(names, heights), key = lambda x:x[1], reverse = True):
            ans.append(x)
        return ans