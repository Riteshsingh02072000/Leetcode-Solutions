class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []

        prefixSum = 0
        suffixSum = sum(nums)

        for i in range(n):
            res.append(i*nums[i] - prefixSum + suffixSum - nums[i]*(n-i))

            suffixSum -= nums[i]
            prefixSum += nums[i]

        return res