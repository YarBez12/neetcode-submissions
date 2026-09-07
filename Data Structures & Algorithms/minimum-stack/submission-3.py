class MinStack:

    # 1st approach 

    # def __init__(self):
    #     self.stack = []
    #     self.stackMins = []
        

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if self.stackMins:
    #         self.stackMins.append(min(self.stackMins[-1], val))
    #     else:
    #         self.stackMins.append(val)

    # def pop(self) -> None:
    #     self.stack.pop()
    #     self.stackMins.pop()

    # def top(self) -> int:
    #     return self.stack[-1]

    # def getMin(self) -> int:
    #     return self.stackMins[-1]

    # 2nd approach

    def __init__(self):
        self.head = None
        

    def push(self, val: int) -> None:
        m = min(val, self.head.min) if self.head else val
        node = ListNode(val, m, self.head)
        self.head = node

    def pop(self) -> None:
        self.head = self.head.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.head.min


class ListNode:
    def __init__(self, val, min, next):
        self.val = val
        self.min = min
        self.next = next
