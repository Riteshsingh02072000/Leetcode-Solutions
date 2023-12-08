# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def trav(node):
            if not node:
                return
            
            self.ans += str(node.val)

            if node.left or node.right:
                self.ans+= '('
                trav(node.left)
                self.ans += ')'
            
            if node.right:
                self.ans += '('
                trav(node.right)
                self.ans += ')'
            
        self.ans = ""
        trav(root)
        return self.ans