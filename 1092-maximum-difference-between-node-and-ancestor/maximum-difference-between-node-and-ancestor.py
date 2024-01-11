# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        ans = [0]
        self.helper(root, ans)
        return ans[0]
    
    def helper(self, root, ans):
        if not root:
            return float('inf'), float('-inf')
        
        left = self.helper(root.left, ans)
        right = self.helper(root.right, ans)

        min_val = min(root.val, min(left[0], right[0]))
        max_val = max(root.val, max(left[1], right[1]))

        ans[0] = max(ans[0], max(abs(root.val-min_val), abs(root.val-max_val)))

        return min_val, max_val