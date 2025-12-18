class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0  # slow pointer
        for j in range(1, len(nums)):  # fast pointer
            if nums[j] != nums[i]:  # found new unique element
                i += 1
                nums[i] = nums[j]   # place unique at next position
        
        return i + 1  # length of unique part
