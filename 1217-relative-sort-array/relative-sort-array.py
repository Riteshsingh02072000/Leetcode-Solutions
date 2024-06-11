class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        prefix = []
        suffix = []

        count = collections.Counter(arr1)

        for x in arr2:
            prefix.extend([x]*count[x])
        
        for y in arr1:
            if y not in arr2:
                suffix.append(y)
        suffix.sort()
        
        return prefix + suffix