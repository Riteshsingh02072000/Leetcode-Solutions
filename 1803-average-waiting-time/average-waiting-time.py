class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        cur = customers[0][0]
        time = 0

        for x, y in customers:
            tmp = max(cur, x)
            cur = tmp + y
            time += (cur - x)
            print(time)
        return time/n