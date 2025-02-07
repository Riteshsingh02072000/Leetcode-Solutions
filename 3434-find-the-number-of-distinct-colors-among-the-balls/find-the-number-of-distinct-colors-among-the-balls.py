class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        node, color = {}, {}
        ans = []

        for x, y in queries:
            if x in node:
                prev = node[x]
                if prev == y:
                    ans.append(len(color))
                    continue
                if color[prev] == 1:
                    del color[prev]
                else:
                    color[prev] -= 1
            
            node[x] = y
            color[y] = color.get(y, 0) +1
            ans.append(len(color))
        return ans
