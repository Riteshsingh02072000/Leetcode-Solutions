class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = collections.Counter(arr)
        v = list(count.values())
        v.sort()
        # print(v)
        ans  = 0 
        n = len(set(arr))
        for i in range(len(v)):
            if k>=v[i]:
                k-=v[i]
                ans+=1
            else:
                k -= v[i]
        return n-ans