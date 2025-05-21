# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inOrder(node):
            if node:
                inOrder(node.left)
                ans.append(node.val)
                inOrder(node.right)
        inOrder(root)
        return sorted(list(set(ans))) == ans
