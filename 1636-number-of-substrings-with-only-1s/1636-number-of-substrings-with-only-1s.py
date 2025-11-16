class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        ans = 0

        for ch in s:
            if ch == '1':
                count += 1
            else:
                ans = (ans + count * (count + 1) // 2) % MOD
                count = 0
        
        # Add final segment if string ends with '1'
        ans = (ans + count * (count + 1) // 2) % MOD
        return ans
