class Solution:
    def validMountainArray(self, arr) -> bool:
        n = len(arr)
        if n < 3:
            return False

        i = 0

        # Step 1: strictly increasing
        while i + 1 < n and arr[i] < arr[i + 1]:
            i += 1

        # Peak cannot be first or last
        if i == 0 or i == n - 1:
            return False

        # Step 2: strictly decreasing
        while i + 1 < n and arr[i] > arr[i + 1]:
            i += 1

        return i == n - 1
