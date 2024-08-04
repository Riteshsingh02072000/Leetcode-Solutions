class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []

        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                arr.append(cur)
        arr.sort()
        return (sum(arr[left-1:right]))%(10**9 +7)