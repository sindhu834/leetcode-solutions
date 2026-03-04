from collections import Counter
from bisect import bisect_right

class Solution:
    def maximumTotalDamage(self, power):
        freq = Counter(power)
        
        vals = sorted(freq.keys())
        n = len(vals)
        
        gains = [v * freq[v] for v in vals]
        dp = [0] * n
        
        for i in range(n):
            # option 1: skip
            skip = dp[i-1] if i > 0 else 0
            
            # option 2: take
            # find last index where vals[j] <= vals[i] - 3
            target = vals[i] - 3
            j = bisect_right(vals, target) - 1
            
            take = gains[i]
            if j >= 0:
                take += dp[j]
            
            dp[i] = max(skip, take)
        
        return dp[-1]