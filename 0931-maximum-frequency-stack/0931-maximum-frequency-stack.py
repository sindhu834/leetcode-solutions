from collections import defaultdict

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)      # val -> frequency
        self.group = defaultdict(list)    # freq -> stack of values
        self.maxfreq = 0                  # track current maximum frequency

    def push(self, val: int) -> None:
        # Step 1: increase frequency
        f = self.freq[val] + 1
        self.freq[val] = f

        # Step 2: update max frequency
        if f > self.maxfreq:
            self.maxfreq = f

        # Step 3: push val into the group of its frequency
        self.group[f].append(val)

    def pop(self) -> int:
        # Step 1: get element from highest frequency group
        val = self.group[self.maxfreq].pop()

        # Step 2: decrease its frequency count
        self.freq[val] -= 1

        # Step 3: if no elements left at this frequency, reduce maxfreq
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return val
