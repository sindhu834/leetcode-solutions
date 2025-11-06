class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.inc = [0] * maxSize  # tracks increment values for each position
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)

    def pop(self) -> int:
        if not self.stack:
            return -1
        i = len(self.stack) - 1
        if i > 0:
            self.inc[i - 1] += self.inc[i]  # propagate increment to next element below
        res = self.stack.pop() + self.inc[i]
        self.inc[i] = 0  # reset after using
        return res

    def increment(self, k: int, val: int) -> None:
        i = min(k, len(self.stack)) - 1
        if i >= 0:
            self.inc[i] += val
