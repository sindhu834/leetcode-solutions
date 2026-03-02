from bisect import bisect_left

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []
        
        for s in spells:
            target = (success + s - 1) // s
            idx = bisect_left(potions, target)
            result.append(m - idx)
        
        return result