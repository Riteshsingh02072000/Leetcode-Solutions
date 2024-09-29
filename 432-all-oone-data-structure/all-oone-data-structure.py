class AllOne:

    def __init__(self):
        self.myDict = {}

    def inc(self, key: str) -> None:
        if key not in self.myDict:
            self.myDict[key] = 1
        else:
            self.myDict[key]+=1

        

    def dec(self, key: str) -> None:
        if self.myDict[key]>1:
            self.myDict[key] -=1
        else:
            del self.myDict[key]        

    def getMaxKey(self) -> str:
        if not self.myDict:
            return ""
        maxVal = max(self.myDict.values())
        for key, val in self.myDict.items():
            if val == maxVal:
                return key
        

    def getMinKey(self) -> str:
        if not self.myDict:
            return ""
        maxVal = min(self.myDict.values())
        for key, val in self.myDict.items():
            if val == maxVal:
                return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()