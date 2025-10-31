class Solution:
    def getSneakyNumbers(self, nums):
        seen = set()
        duplicates = []
        
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
                
        return duplicates
