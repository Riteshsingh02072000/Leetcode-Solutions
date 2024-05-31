class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans = set()
        for num in nums:
            if num in ans:
                ans.remove(num)
                continue
            ans.add(num)
        return list(ans)