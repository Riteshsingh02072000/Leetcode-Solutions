class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        return max(self.helper(red, blue), self.helper(blue, red))

    def helper(self, first, second):
        h = 0
        i = 1

        while True:
            if i%2==1:
                if first>=i:
                    first -= i
                else:
                    break
            else:
                if second >= i:
                    second -= i
                else:
                    break
            h+=1
            i += 1
        return h