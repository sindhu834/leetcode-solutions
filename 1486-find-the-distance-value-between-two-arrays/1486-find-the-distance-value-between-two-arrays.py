class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0
        
        # For each element in arr1
        for i in arr1:
            valid = True  # assume this element satisfies the condition
            
            # Compare with every element in arr2
            for j in arr2:
                if abs(i - j) <= d:  # if distance condition fails
                    valid = False
                    break  # no need to check further
            
            if valid:
                count += 1  # count only if condition is satisfied
        
        return count
