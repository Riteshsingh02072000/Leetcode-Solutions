# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(node):
            if node.left and node.right:
                helper(node.left)
                helper(node.right)
            elif node.left:
                helper(node.left)
            elif node.right:
                helper(node.right)
            else:
                self.ans.append(node.val)
        
        self.ans = []
        helper(root1)
        length = len(self.ans)
        helper(root2)
        return self.ans[:length] == self.ans[length:]