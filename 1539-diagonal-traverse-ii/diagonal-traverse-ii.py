class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        ans = []
        dic = collections.defaultdict(list)

        for r in range(len(nums)-1, -1, -1):
            for c in range(len(nums[r])):
                diag = r+c
                dic[diag].append(nums[r][c])
            
        tmp = 0
        while tmp in dic:
            ans.extend(dic[tmp])
            tmp+=1
        return ans