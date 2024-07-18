# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.map ={}
        self.leaves = []
        print(self.leaves)
        ans = 0
        self.dfs(root, [], self.leaves, self.map)
        n = len(self.leaves)
        for i in range(n):
            for j in range(i+1, n):
                list_i, list_j = self.map[self.leaves[i]], self.map[self.leaves[j]]
                for k in range(min(len(list_i), len(list_j))):
                    if list_i[k]!=list_j[k]:
                        dist = len(list_i) - k + len(list_j)-k
                        if dist<=distance:
                            ans += 1
                        break
        return ans

    
    def dfs(self, node, trail, leaves, maps):
        if not node:
            return
        
        tmp = trail[:]
        tmp.append(node)

        if not node.left and not node.right:
            maps[node] = tmp
            leaves.append(node)
            return
        
        self.dfs(node.left, tmp, leaves, maps)
        self.dfs(node.right, tmp, leaves, maps)
