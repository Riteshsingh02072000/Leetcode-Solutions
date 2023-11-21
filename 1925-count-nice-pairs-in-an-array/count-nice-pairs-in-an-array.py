class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        count = 0
        def rev(x):
            reverse = 0
            temp = x
            while temp!=0:
                reverse *=10
                reverse += (temp%10)
                temp = temp//10
            
            return x-reverse

        hashmap = collections.defaultdict(int)
        mod = 10**9+7
        for num in nums:
            val = rev(num)
            if hashmap[val]:
                count+=hashmap[val]%mod
            hashmap[val] += 1
        return count%mod