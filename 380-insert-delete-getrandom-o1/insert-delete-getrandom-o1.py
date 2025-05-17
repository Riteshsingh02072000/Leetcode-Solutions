import random
class RandomizedSet:

    def __init__(self):
        self.randomized = set()
        

    def insert(self, val: int) -> bool:
        if val not in self.randomized:
            self.randomized.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        if val in self.randomized:
            self.randomized.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(list(self.randomized))

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()