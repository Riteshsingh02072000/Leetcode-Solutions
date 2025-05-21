# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # ans = []
        # def inOrder(node):
        #     if not node:
        #         return None
            
        #     inOrder(node.left)
        #     ans.append(node.val)
        #     inOrder(node.right)
        # inOrder(root)
        # return ans[k-1]
        val = []
        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            val.append(root.val)
            inOrder(root.right)
            if len(val)>=k:
                return val[k-1]
        inOrder(root)
        return val[k-1]

        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.left
            
        #     cur = stack.pop()
        #     n+=1
        #     if n==k:
        #         return cur.val
        #     cur = cur.right