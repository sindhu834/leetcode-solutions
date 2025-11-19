class Solution:
    def findFinalValue(self, nums, original):
        nums_set = set(nums)     # Convert to set for fast lookup
        
        while original in nums_set:
            original *= 2
        
        return original
