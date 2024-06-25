# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        # trav = []
        # def dfs(node):
        #     if not node:
        #         return
        #     dfs(node.left)
        #     trav.append(node.val)
        #     dfs(node.right)
        # dfs(root)
        
        # def traverse(node):
        #     if not node:
        #         return
        #     idx = trav.index(node.val)
        #     node.val = sum(trav[idx:])

        #     traverse(node.left)
        #     traverse(node.right)
        # traverse(root)
        # return root

        self.val = 0 

        def dfs(node):
            if not node:
                return
            
            dfs(node.right)
            self.val+=node.val
            node.val = self.val
            dfs(node.left)
        dfs(root)
        return root