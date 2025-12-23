class Solution:
    def longestSubarray(self, nums):
        mx = max(nums)
        max_len = 0
        curr_len = 0
        
        for num in nums:
            if num == mx:
                curr_len += 1
                max_len = max(max_len, curr_len)
            else:
                curr_len = 0
        
        return max_len
