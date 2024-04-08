class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]

        for x in students:
            count[x] += 1
        
        ans = len(sandwiches)

        for x in sandwiches:
            if count[x] == 0:
                break
            if ans == 0:
                break
            ans -= 1
            count[x] -=1
        return ans