class MinStack:

    def __init__(self):
       self.inner = []
       self.mins = []

    def push(self, val: int) -> None:
        self.inner.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            m = min(self.mins[-1], val)
            self.mins.append(m)

    def size(self):
        return len(self.inner)

    def pop(self) -> None:
        self.inner.pop()
        self.mins.pop()


    def top(self) -> int:
        return self.inner[-1]


    def getMin(self) -> int:
        return self.mins[self.size() - 1]
