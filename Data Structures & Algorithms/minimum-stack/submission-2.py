class MinStack:

    def __init__(self):
        self.stack = []
        self.stackMins = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.stackMins:
            self.stackMins.append(min(self.stackMins[-1], val))
        else:
            self.stackMins.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.stackMins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stackMins[-1]
