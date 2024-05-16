# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)

        ans = False
        if root.val == 2:
            ans = left or right
        else:
            ans = left and right
        return ans