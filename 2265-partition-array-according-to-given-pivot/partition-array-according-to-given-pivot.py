class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        prefix = []
        suffix = []
        same = 0

        for x in nums:
            if x<pivot:
                prefix.append(x)
            elif x>pivot:
                suffix.append(x)
            else:
                same+=1
        return prefix + [pivot]*same + suffix