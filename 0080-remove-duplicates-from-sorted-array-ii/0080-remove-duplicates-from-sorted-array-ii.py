class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        
        # If array has 2 or fewer elements, all are allowed
        if n <= 2:
            return n

        k = 2  # First two elements are always valid

        for i in range(2, n):
            # Allow nums[i] only if it does not create more than 2 duplicates
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1

        return k
