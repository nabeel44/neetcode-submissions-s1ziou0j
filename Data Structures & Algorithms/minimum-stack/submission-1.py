class MinStack:

    def __init__(self):
        self.stack = []
        self.lowest = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.lowest or val <= self.lowest[-1]:
            self.lowest.append(val)

        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.lowest[-1]:
            self.lowest.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.lowest[-1]
        
