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
        value = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            value.append(node.val)
            dfs(node.right)
        dfs(root)
        return value
        

    def next(self) -> int:
        node = self.val[self.idx]
        self.idx+=1
        return node

        

    def hasNext(self) -> bool:
        return self.idx<len(self.val)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()