# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        occ = [0]*10
        return self.dfs(root, occ)

    def dfs(self, node, occ):
        if not node:
            return 0
        
        occ[node.val] += 1

        if not node.left and not node.right:
            cnt = self.countOdd(occ)
            occ[node.val] -=1
            return 1 if cnt<=1 else 0
        
        left = self.dfs(node.left, occ)
        right = self.dfs(node.right, occ)

        occ[node.val] -=1
        return left+right
    

    def countOdd(self, occ):
        count = 0
        for x in occ:
            if x%2==1:
                count+=1
        return count