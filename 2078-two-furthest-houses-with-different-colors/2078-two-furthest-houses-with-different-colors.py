class Solution:
    def maxDistance(self, colors):
        n = len(colors)
        ans = 0
        
        # check from left
        for i in range(n):
            if colors[i] != colors[0]:
                ans = max(ans, i)
        
        # check from right
        for i in range(n):
            if colors[i] != colors[-1]:
                ans = max(ans, n - 1 - i)
        
        return ans