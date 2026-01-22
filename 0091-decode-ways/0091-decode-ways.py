class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # empty string
        dp[1] = 1  # first character (since s[0] != '0')
        
        for i in range(2, n + 1):
            # One-digit decode
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            # Two-digit decode
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]
