class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        total = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            newBottles = empty // numExchange
            total += newBottles
            empty = newBottles + (empty % numExchange)
        
        return total