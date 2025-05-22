# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.idx = 0
        self.val = self.traverse(root)
    
    def traverse(self, root):
        val = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            val.append(node.val)
            dfs(node.right)
        dfs(root)
        return val
        

    def next(self) -> int:
        nextVal = self.val[self.idx]
        self.idx += 1
        return nextVal

        

    def hasNext(self) -> bool:
        return len(self.val)>self.idx
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()