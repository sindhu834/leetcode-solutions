class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            # exchange once
            empty -= numExchange
            numExchange += 1
            
            # drink the new bottle
            total += 1
            empty += 1
        
        return total