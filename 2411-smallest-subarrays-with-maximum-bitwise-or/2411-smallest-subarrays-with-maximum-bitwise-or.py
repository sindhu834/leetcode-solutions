class Solution:
    def smallestSubarrays(self, nums):
        n = len(nums)
        answer = [0] * n
        
        # last occurrence of each bit (0 to 30)
        last = [-1] * 32
        
        for i in range(n - 1, -1, -1):
            # update last occurrence of bits in nums[i]
            for b in range(32):
                if (nums[i] >> b) & 1:
                    last[b] = i
            
            # find farthest index needed
            farthest = i
            for b in range(32):
                if last[b] != -1:
                    farthest = max(farthest, last[b])
            
            answer[i] = farthest - i + 1
        
        return answer
