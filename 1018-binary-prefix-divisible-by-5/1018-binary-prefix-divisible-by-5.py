class Solution:
    def prefixesDivBy5(self, nums):
        rem = 0
        result = []
        
        for bit in nums:
            rem = (rem * 2 + bit) % 5
            result.append(rem == 0)
        
        return result
