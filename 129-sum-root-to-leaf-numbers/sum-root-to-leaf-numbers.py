# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0)
        return self.ans
    
    def dfs(self, node, path):
        if node:
            if not node.left and not node.right:
                path = path*10 + node.val
                self.ans += path
            
            self.dfs(node.left, path*10+node.val)
            self.dfs(node.right, path*10+node.val)

        