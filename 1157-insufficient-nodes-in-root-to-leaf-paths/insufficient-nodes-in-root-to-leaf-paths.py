# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        return self.helper(root, 0, limit)
        
    def helper(self, node, curSum , limit):
        if not node:
            return None
        curSum += node.val
        if not node.left and not node.right:
            return node if curSum >= limit else None
        node.left = self.helper(node.left, curSum, limit)
        node.right = self.helper(node.right, curSum , limit)
        if not node.left and not node.right:
            return None
        return node