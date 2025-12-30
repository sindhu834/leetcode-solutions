import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.stacks = []
        self.push_heap = []   # min heap (leftmost non-full stack)
        self.pop_heap = []    # max heap (rightmost non-empty stack)

    def push(self, val: int) -> None:
        # Remove invalid full stacks
        while self.push_heap and (
            self.push_heap[0] >= len(self.stacks) or
            len(self.stacks[self.push_heap[0]]) == self.capacity
        ):
            heapq.heappop(self.push_heap)

        # If no available stack, create a new one
        if not self.push_heap:
            index = len(self.stacks)
            self.stacks.append([])
        else:
            index = self.push_heap[0]

        # Push value
        self.stacks[index].append(val)

        # Add to pop heap (max heap via negative)
        heapq.heappush(self.pop_heap, -index)

        # If stack still not full, keep it in push heap
        if len(self.stacks[index]) < self.capacity:
            heapq.heappush(self.push_heap, index)

    def pop(self) -> int:
        # Remove invalid empty stacks
        while self.pop_heap and (
            -self.pop_heap[0] >= len(self.stacks) or
            not self.stacks[-self.pop_heap[0]]
        ):
            heapq.heappop(self.pop_heap)

        if not self.pop_heap:
            return -1

        index = -heapq.heappop(self.pop_heap)
        val = self.stacks[index].pop()

        # Stack has space now → add to push heap
        heapq.heappush(self.push_heap, index)

        # If still not empty, add back to pop heap
        if self.stacks[index]:
            heapq.heappush(self.pop_heap, -index)

        return val

    def popAtStack(self, index: int) -> int:
        if index >= len(self.stacks) or not self.stacks[index]:
            return -1

        val = self.stacks[index].pop()

        # Stack now has space
        heapq.heappush(self.push_heap, index)

        # If still not empty, add to pop heap
        if self.stacks[index]:
            heapq.heappush(self.pop_heap, -index)

        return val
