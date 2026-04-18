class Solution:
    def mirrorDistance(self, n):
        # reverse the number
        rev = int(str(n)[::-1])
        
        return abs(n - rev)