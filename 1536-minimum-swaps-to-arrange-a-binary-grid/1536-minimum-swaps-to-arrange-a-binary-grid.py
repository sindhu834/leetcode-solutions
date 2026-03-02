class Solution:
    def minSwaps(self, grid):
        n = len(grid)
        
        # Step 1: compute trailing zeros
        trailing = []
        for row in grid:
            count = 0
            for val in reversed(row):
                if val == 0:
                    count += 1
                else:
                    break
            trailing.append(count)
        
        swaps = 0
        
        # Step 2: greedy placement
        for i in range(n):
            needed = n - 1 - i
            j = i
            
            # find row that satisfies requirement
            while j < n and trailing[j] < needed:
                j += 1
            
            if j == n:
                return -1
            
            # bring row j up to i
            while j > i:
                trailing[j], trailing[j-1] = trailing[j-1], trailing[j]
                swaps += 1
                j -= 1
        
        return swaps