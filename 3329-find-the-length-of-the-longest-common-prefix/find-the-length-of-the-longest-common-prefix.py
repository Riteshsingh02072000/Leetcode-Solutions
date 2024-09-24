class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        dic = defaultdict(int)

        for num in arr1:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix+=ch
                dic[prefix] += 1
        ans = 0

        for num in arr2:
            str_num = str(num)
            prefix = ""
            for ch in str_num:
                prefix+=ch
                if prefix in dic:
                    ans = max(ans, len(prefix))
        return ans