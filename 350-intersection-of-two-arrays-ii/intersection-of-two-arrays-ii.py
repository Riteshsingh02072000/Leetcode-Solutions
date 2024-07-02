class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        ans = []
        for i in count1.keys() and count2.keys():
            ans.extend([i]*min(count1[i], count2[i]))
        return ans