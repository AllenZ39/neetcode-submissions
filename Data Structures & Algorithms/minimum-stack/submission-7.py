import math
class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = [math.inf]

    def push(self, val: int) -> None:
        self.items.append(val)
        self.minStack.append(min(val, self.minStack[-1]))


    def pop(self) -> None:
        self.items.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.items[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
