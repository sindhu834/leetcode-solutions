class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def solve(n, k):
            if n == 1:
                return 0
            
            mid = 1 << (n - 1)  # 2^(n-1)
            
            if k == mid:
                return 1
            elif k < mid:
                return solve(n - 1, k)
            else:
                mirror = (1 << n) - k
                return 1 - solve(n - 1, mirror)
        
        return str(solve(n, k))