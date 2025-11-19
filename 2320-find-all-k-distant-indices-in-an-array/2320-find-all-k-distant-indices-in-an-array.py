class Solution:
    def findKDistantIndices(self, nums, key, k):
        key_indices = []

        # Step 1: collect all indices where nums[j] == key
        for i in range(len(nums)):
            if nums[i] == key:
                key_indices.append(i)
        
        ans = []

        # Step 2: check each index if it is close to any key index
        j = 0  # pointer for key_indices

        for i in range(len(nums)):
            # Move pointer until |i - key_indices[j]| <= k
            while j < len(key_indices) and key_indices[j] < i - k:
                j += 1
            
            # If current key index is within distance k
            if j < len(key_indices) and abs(key_indices[j] - i) <= k:
                ans.append(i)

        return ans
