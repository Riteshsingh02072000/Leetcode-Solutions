class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        val = len(set(nums))
        count = 0
        n = len(nums)
        l = 0
        r = 0
        counter = Counter()

        while r<n:
            counter[nums[r]] += 1
            while len(counter) == val:
                counter[nums[l]] -= 1
                if counter[nums[l]] == 0:
                    del counter[nums[l]]
                l += 1
                count += n-r
            r += 1
        return count