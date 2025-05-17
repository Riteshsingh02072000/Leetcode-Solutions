import random
class RandomizedSet:

    def __init__(self):
        # self.randomized = set()
        self.lst = []
        self.idxMap = {}
        
    # def search(self, val):
    #     return val in self.idx
    def insert(self, val: int) -> bool:
        # if val not in self.randomized:
        #     self.randomized.add(val)
        #     return True
        # return False
        if val in self.idxMap:
            return False
        self.lst.append(val)
        self.idxMap[val] = len(self.lst)-1
        return True
        

    def remove(self, val: int) -> bool:
        # if val in self.randomized:
        #     self.randomized.remove(val)
        #     return True
        # return False
        if val not in self.idxMap:
            return False
        idx = self.idxMap[val]
        self.lst[idx] = self.lst[-1]
        self.idxMap[self.lst[-1]] = idx
        self.lst.pop()
        del self.idxMap[val]
        return True
        

    def getRandom(self) -> int:
        return random.choice(self.lst)

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()