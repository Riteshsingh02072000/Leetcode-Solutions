class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for x in nums:
            if x<0:
                neg.append(x)
            else:
                pos.append(x)
        
        for a, b in zip(pos, neg):
            ans.append(a)
            ans.append(b)
        return ans