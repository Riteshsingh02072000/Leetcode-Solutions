class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        self.pheap = []
        self.tmap = {}
        
        for task in tasks:
            uid, tid, p = tuple(task)
            self.add(uid, tid, p)
        

    def add(self, userId: int, taskId: int, priority: int) -> None:

        heapq.heappush(self.pheap, (-priority, -taskId, userId))
        self.tmap[taskId] = (priority, userId)
        

    def edit(self, taskId: int, newPriority: int) -> None:
        oldPriority, uid = self.tmap[taskId]
        self.tmap[taskId] = (newPriority, uid)
        heappush(self.pheap, (-newPriority, -taskId, uid))
        

    def rmv(self, taskId: int) -> None:
        self.tmap[taskId] = None
        

    def execTop(self) -> int:

        #print(self.pheap)

        while self.pheap:
            neg_priority, neg_taskId, userId = heappop(self.pheap)
            priority, taskId = -neg_priority, -neg_taskId

            if taskId in self.tmap and self.tmap[taskId] == (priority, userId):
                del self.tmap[taskId]

                return userId
        return -1

        # if not self.pheap: 
        #     return -1


        # p, t, u = heapq.heappop(self.pheap)
        # if self.tmap[-t] and self.tmap[-t][0] == -p:
        #     self.tmap[-t] = None
        #     return u


        # return self.execTop()


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()