# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        self.recovery(root, 0)
    
    def recovery(self, node, val):
        if not node:
            return 
        self.values.add(val)
        self.recovery(node.left, val*2 +1)
        self.recovery(node.right, val*2 +2)

        
    def find(self, target: int) -> bool:
        return target in self.values

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)