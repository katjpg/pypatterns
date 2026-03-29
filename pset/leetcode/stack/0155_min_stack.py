class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minStack[-1]:
            self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


"""
time: O(1)
- push, pop, top, getMin are all constant time.
- minStack only appends/pops when current min changes.

space: O(n)
- stack stores all elements.
- minStack stores at most n elements (worst case: descending input).

"""
