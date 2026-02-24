class Solution:
    def largestPerimeter(self, nums):
        nums.sort()
        
        # Start from the end (largest values)
        for i in range(len(nums) - 1, 1, -1):
            if nums[i-2] + nums[i-1] > nums[i]:
                return nums[i-2] + nums[i-1] + nums[i]
        
        return 0