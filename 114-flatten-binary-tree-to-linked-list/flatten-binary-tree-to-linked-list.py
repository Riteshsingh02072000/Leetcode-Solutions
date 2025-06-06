# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = TreeNode()
        ans = cur

        vals = []
        def preOrder(node):
            if not node:
                return
            vals.append(node)
            preOrder(node.left)
            preOrder(node.right)
        preOrder(root)

        for i in range(1, len(vals)):
            prev = vals[i-1]
            cur = vals[i]
            prev.left = None
            prev.right = cur