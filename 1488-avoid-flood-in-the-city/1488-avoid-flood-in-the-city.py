from bisect import bisect_right
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains):
        n = len(rains)
        ans = [-1] * n
        
        full = {}              # lake -> last rain day
        dry_days = SortedList()  # store indices of zero days
        
        for i in range(n):
            if rains[i] > 0:
                lake = rains[i]
                
                if lake in full:
                    prev = full[lake]
                    
                    # find dry day after prev
                    idx = dry_days.bisect_right(prev)
                    
                    if idx == len(dry_days):
                        return []
                    
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake
                    dry_days.remove(dry_day)
                
                full[lake] = i
                ans[i] = -1
            
            else:
                dry_days.add(i)
                ans[i] = 1  # temporary, may change later
        
        return ans