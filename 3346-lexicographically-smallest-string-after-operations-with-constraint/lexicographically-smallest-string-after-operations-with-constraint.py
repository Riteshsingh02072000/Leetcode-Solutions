class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        ans = []
        count = 0
        dic = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        def findMin(c1, c2):
            dis1 = (ord(c1)-ord(c2))%26
            dis2 = (ord(c2)-ord(c1))%26

            return min(dis1, dis2)
        
        for c in s:
            for char in dic:
                curMin = findMin(c, char)
                if count+curMin<=k:
                    count+=curMin
                    ans.append(char)
                    break
        return ''.join(ans)