class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        valid = 0

        def simulate(start, direction):
            arr = nums[:]  # copy array to avoid modifying original
            curr = start
            dir = direction  # +1 for right, -1 for left

            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += dir  # move in the same direction
                else:
                    arr[curr] -= 1
                    dir *= -1    # reverse direction
                    curr += dir

            return all(x == 0 for x in arr)

        # Try each zero position with both directions
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):   # moving right
                    valid += 1
                if simulate(i, -1):  # moving left
                    valid += 1

        return valid
