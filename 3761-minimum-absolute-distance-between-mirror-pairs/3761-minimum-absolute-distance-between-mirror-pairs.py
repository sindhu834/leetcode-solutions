class Solution:
    def minMirrorPairDistance(self, nums):
        def reverse_num(x):
            return int(str(x)[::-1])
        
        seen = {}
        ans = float('inf')
        
        for i, num in enumerate(nums):
            # we need reverse(previous) == current
            # so store reverse(previous)
            
            if num in seen:
                ans = min(ans, i - seen[num])
            
            rev = reverse_num(num)
            seen[rev] = i
        
        return ans if ans != float('inf') else -1