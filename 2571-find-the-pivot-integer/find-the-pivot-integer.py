class Solution:
    def pivotInteger(self, n: int) -> int:
        for i in range(1, n + 1):
            left_sum = i * (i + 1) // 2  # Calculate the sum of elements from 1 to i using arithmetic progression formula
            right_sum = n * (n + 1) // 2 - i * (i - 1) // 2  # Calculate the sum of elements from i to n using arithmetic progression formula
            if left_sum == right_sum:
                return i  # Return i as the pivot integer
        return -1  # If no such integer exists, return -1      