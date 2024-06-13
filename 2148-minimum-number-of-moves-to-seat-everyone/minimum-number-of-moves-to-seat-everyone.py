class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        ans = 0
        students.sort()
        seats.sort()

        for i in range(len(seats)):
            ans += abs(seats[i] - students[i])
        return ans