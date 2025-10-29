class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = (x << 1) | 1   # Left shift and set all bits to 1
        return x
