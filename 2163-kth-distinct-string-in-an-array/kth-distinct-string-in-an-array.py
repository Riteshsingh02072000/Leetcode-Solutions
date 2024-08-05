class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)

        for v in arr:
            if c[v] == 1:
                k-=1
                if k == 0:
                    return v
        return ''