# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val = []
        def getValue(node):
            if not node:
                return
            getValue(node.left)
            val.append(node.val)
            getValue(node.right)
        
        getValue(root)

        ans = val[1]-val[0]
        for i in range(1, len(val)):
            diff = val[i] - val[i-1]
            ans = min(ans, diff)
        return ans