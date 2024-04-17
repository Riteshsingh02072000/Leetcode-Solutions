# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node, string):
            if not node:
                return 
            
            string = chr(node.val + 97) + string

            if not node.left and not node.right:
                res.append(string)
                return
            if node.left:
                dfs(node.left, string)
            if node.right:
                dfs(node.right, string)
        
        dfs(root, "")

        return sorted(res)[0]
        