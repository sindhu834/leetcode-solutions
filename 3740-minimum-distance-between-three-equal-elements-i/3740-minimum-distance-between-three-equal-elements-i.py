from collections import defaultdict

class Solution:
    def minimumDistance(self, nums):
        pos = defaultdict(list)
        
        # store indices
        for i, num in enumerate(nums):
            pos[num].append(i)
        
        ans = float('inf')
        
        for indices in pos.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    left = indices[i]
                    right = indices[i+2]
                    ans = min(ans, right - left)
        
        if ans == float('inf'):
            return -1
        
        return 2 * ans