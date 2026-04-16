import bisect
from collections import defaultdict

class Solution:
    def solveQueries(self, nums, queries):   # ✅ correct name
        n = len(nums)
        
        pos = defaultdict(list)
        for i, val in enumerate(nums):
            pos[val].append(i)
        
        ans = []
        
        for q in queries:
            val = nums[q]
            indices = pos[val]
            
            if len(indices) == 1:
                ans.append(-1)
                continue
            
            idx = bisect.bisect_left(indices, q)
            
            left = indices[idx - 1] if idx > 0 else indices[-1]
            right = indices[idx + 1] if idx < len(indices) - 1 else indices[0]
            
            d1 = abs(q - left)
            d2 = abs(q - right)
            
            dist = min(d1, d2, n - d1, n - d2)
            
            ans.append(dist)
        
        return ans