class Solution:
    def mergeSort(self, array):
        n = len(array)
        if n<=1:
            return array
        mid = n//2

        left = array[:mid]
        right = array[mid:]
        l = self.mergeSort(left)
        r = self.mergeSort(right)

        self.merge(l, r, array)
        return array
    
    def merge(self, arr1, arr2, source):
        p1, p2 = 0,0
        n1, n2 = len(arr1), len(arr2)

        i = 0
        while p1<n1 or p2<n2:
            if p1 == n1 or (p2!=n2 and arr2[p2]<arr1[p1]):
                source[i] = arr2[p2]
                p2+=1
            elif p2 == n2 or (arr1[p1]<=arr2[p2]):
                source[i] = arr1[p1]
                p1+=1
            i+=1
        



    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
        # return nums
        # heap = nums[:]
        # heapq.heapify(heap)
        # for i in range(len(nums)):
        #     nums[i] = heapq.heappop(heap)

        # return nums
