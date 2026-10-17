class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('inf')
        

    def push(self, value: int) -> None:
        self.stack.append((value, self.min))
        self.min = min(self.min, value)
        

    def pop(self) -> None:
        self.min = self.stack[-1][1]
        self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()