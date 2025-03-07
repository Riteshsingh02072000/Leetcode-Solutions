class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        cnt = collections.defaultdict(int)
        n = len(nums)
        for num in nums:
            cnt[num] += 1
            if cnt[num]>n/3:
                if num not in ans:
                    ans.append(num)
        return ans
