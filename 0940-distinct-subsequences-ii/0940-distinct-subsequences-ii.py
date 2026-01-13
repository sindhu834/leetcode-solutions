class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1  # empty subsequence

        last = {}  # last occurrence index (1-based)

        for i in range(1, n + 1):
            c = s[i - 1]
            dp[i] = (dp[i - 1] * 2) % MOD

            if c in last:
                dp[i] = (dp[i] - dp[last[c] - 1]) % MOD

            last[c] = i

        # remove empty subsequence
        return (dp[n] - 1) % MOD
